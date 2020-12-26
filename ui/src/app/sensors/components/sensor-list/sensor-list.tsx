import {Page, SlidingPanel, Tabs} from 'argo-ui';
import * as React from 'react';
import {useContext, useEffect, useState} from 'react';
import {Link, RouteComponentProps} from 'react-router-dom';
import {Sensor} from '../../../../models';
import {uiUrl} from '../../../shared/base';
import {Observable} from 'rxjs';
import {kubernetes} from '../../../../models';
import {ErrorNotice} from '../../../shared/components/error-notice';
import {Loading} from '../../../shared/components/loading';
import {NamespaceFilter} from '../../../shared/components/namespace-filter';
import {EventsPanel} from '../../../workflows/components/events-panel';
import {Timestamp} from '../../../shared/components/timestamp';
import {ZeroState} from '../../../shared/components/zero-state';
import {Context} from '../../../shared/context';
import {historyUrl} from '../../../shared/history';
import {services} from '../../../shared/services';
import {SensorCreator} from '../sensor-creator';
import {Node} from '../../../shared/components/graph/types';
import {FullHeightLogsViewer} from '../../../workflows/components/workflow-logs-viewer/full-height-logs-viewer';
import {ID} from '../../../events/components/events-details/id';

require('./sensor-list.scss');

const learnMore = <a href='https://argoproj.github.io/argo-events/concepts/sensor/'>Learn more</a>;

function identity<T>(value: T) {
    return () => value;
}

export const SensorList = ({match, location, history}: RouteComponentProps<any>) => {
    // boiler-plate
    const queryParams = new URLSearchParams(location.search);
    const {navigation} = useContext(Context);

    // state for URL and query parameters
    const [namespace, setNamespace] = useState(match.params.namespace || '');
    const [sidePanel, setSidePanel] = useState(queryParams.get('sidePanel') === 'true');
    const [selectedNode, setSelectedNode] = useState<Node>(queryParams.get('selectedNode'));
    const [tab, setTab] = useState<Node>(queryParams.get('tab'));
    useEffect(
        () =>
            history.push(
                historyUrl('sensors/{namespace}', {
                    namespace,
                    sidePanel,
                    selectedNode,
                    tab
                })
            ),
        [namespace, sidePanel, selectedNode, tab]
    );

    // internal state
    const [error, setError] = useState<Error>();
    const [sensors, setSensors] = useState<Sensor[]>();
    
    useEffect(() => {
        services.sensor
            .list(namespace)
            .then(l => setSensors(l.items?l.items:[]))
            .then(() => setError(null))
            .catch(setError);
    }, [namespace]);

    const selected = (() => {
        if (!selectedNode) {
            return;
        }
        const x = ID.split(selectedNode);
        const value = (sensors || []).find((y: {metadata: kubernetes.ObjectMeta}) => y.metadata.namespace === x.namespace && y.metadata.name === x.name);
        return {value, ...x};
    })();

    const [logsObservable, setLogsObservable] = useState<Observable<string>>();
    const [logLoaded, setLogLoaded] = useState(false);
    useEffect(() => {
        if (!selectedNode) {
            return;
        }
        setError(null);
        setLogLoaded(false);
        const source = services.sensor.sensorsLogs(namespace, selected.name, selected.key, '', 50)
            .filter(e => !!e)
            .map(
                e =>
                    Object.entries(e)
                        .map(([key, value]) => key + '=' + value)
                        .join(', ') + '\n'
            )
            .publishReplay().refCount();
        const subscription = source.subscribe(() => setLogLoaded(true), setError);
        setLogsObservable(source);
        return () => subscription.unsubscribe();
    }, [selectedNode]);

    return (
        <Page
            title='Sensors'
            toolbar={{
                breadcrumbs: [
                    {title: 'Sensors', path: uiUrl('sensors')},
                    {title: namespace, path: uiUrl('sensors/' + namespace)}
                ],
                actionMenu: {
                    items: [
                        {
                            title: 'Create New Sensor',
                            iconClassName: 'fa fa-plus',
                            action: () => setSidePanel(true)
                        }
                    ]
                },
                tools: [<NamespaceFilter key='namespace-filter' value={namespace} onChange={setNamespace} />]
            }}>
            <ErrorNotice error={error} />
            {!sensors ? (
                <Loading />
            ) : sensors.length === 0 ? (
                <ZeroState title='No sensors'>
                    <p>You can create new sensors here.</p>
                    <p>
                        {learnMore}.
                    </p>
                </ZeroState>
            ) : (
                <>
                    <div className='argo-table-list'>
                        <div className='row argo-table-list__head'>
                            <div className='columns small-1' />
                            <div className='columns small-4'>NAME</div>
                            <div className='columns small-3'>NAMESPACE</div>
                            <div className='columns small-2'>CREATED</div>
                            <div className='columns small-2'>LOGS</div>
                        </div>
                        {sensors.map(s => (
                            <Link
                                className='row argo-table-list__row'
                                key={`${s.metadata.namespace}/${s.metadata.name}`}
                                to={uiUrl(`sensors/${s.metadata.namespace}/${s.metadata.name}`)}>
                                <div className='columns small-1'>
                                    <i className='fa fa-clone' />
                                </div>
                                <div className='columns small-4'>{s.metadata.name}</div>
                                <div className='columns small-3'>{s.metadata.namespace}</div>
                                <div className='columns small-2'>
                                    <Timestamp date={s.metadata.creationTimestamp} />
                                </div>
                                <div className='columns small-2'>
                                    <div onClick={e => {
                                        e.preventDefault();
                                        setSelectedNode(`${s.metadata.namespace}/Sensor/${s.metadata.name}`);
                                    }}>
                                        <i className='fa fa-bars' />
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                    <p>
                    </p>
                </>
            )}
            <SlidingPanel isShown={sidePanel} onClose={() => setSidePanel(false)}>
                <SensorCreator namespace={namespace} onCreate={s => navigation.goto(uiUrl(`sensors/${s.metadata.namespace}/${s.metadata.name}`))} />
            </SlidingPanel>
            <SlidingPanel isShown={!!selectedNode} onClose={() => setSelectedNode(null)}>
                {!!selectedNode && (
                    <div>
                        <h4>
                            Sensor/{selected.name}{selected.key?'/'+selected.key:''}
                        </h4>
                        <Tabs
                            navTransparent={true}
                            selectedTabKey={tab}
                            onTabSelected={setTab}
                            tabs={[
                                {
                                    title: 'LOGS',
                                    key: 'logs',
                                    content: (
                                        <div>
                                            <div className='row'>
                                                <div className='columns small-3 medium-2'>
                                                    <p>Triggers</p>
                                                    <div key='all' style={{marginBottom: '1em'}}>
                                                        <div key='all'
                                                            onClick={() => {
                                                                setSelectedNode(`${namespace}/Sensor/${selected.name}`);
                                                                }}>
                                                            {!selected.key && <i className='fa fa-angle-right' />}
                                                            {!!selected.key && <span>&nbsp;&nbsp;</span>}
                                                            <a><span title='all'>all</span></a>
                                                        </div>
                                                        {!!selected.value && selected.value.spec.triggers.map(x => (
                                                            <div key={x.template.name}
                                                                onClick={() => {
                                                                    setSelectedNode(`${namespace}/Trigger/${selected.name}/${x.template.name}`);
                                                                }}>
                                                                {selected.key === x.template.name && <i className='fa fa-angle-right' />}
                                                                {selected.key != x.template.name && <span>&nbsp;&nbsp;</span>}
                                                                <a><span title={x.template.name}>{x.template.name}</span></a>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                                <div className='columns small-9 medium-10' style={{height: 600}}>
                                                    {!logLoaded ? (
                                                        <p>
                                                            <i className='fa fa-circle-notch fa-spin' /> Waiting for data...
                                                        </p>
                                                    ) : (
                                                        <FullHeightLogsViewer
                                                            source={{
                                                                key: 'logs',
                                                                loadLogs: identity(logsObservable),
                                                                shouldRepeat: () => false
                                                            }}
                                                        />
                                                    )}
                                                </div>                     
                                            </div>
                                        </div>
                                    )
                                },
                                {
                                    title: 'EVENTS',
                                    key: 'events',
                                    content: <EventsPanel kind='Sensor' namespace={selected.namespace} name={selected.name} />
                                }
                            ]}
                        />
                    </div>
                )}
            </SlidingPanel>
        </Page>
    );
};
