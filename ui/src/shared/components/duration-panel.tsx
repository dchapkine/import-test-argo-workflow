import * as React from 'react';

import {formatDuration} from '../duration';
import {NODE_PHASE, NodePhase} from '../models';
import {ProgressLine} from './progress-line';

// duration panel in seconds
export function DurationPanel(props: {phase: NodePhase; duration: number; estimatedDuration?: number}) {
    if (props.phase === NODE_PHASE.RUNNING && props.estimatedDuration) {
        return (
            <>
                <span title={'Estimate duration: ' + formatDuration(props.estimatedDuration)}>
                    <ProgressLine progress={props.duration / props.estimatedDuration} width={32} height={8} />
                </span>{' '}
                {formatDuration(props.duration)}
            </>
        );
    }
    return <>{formatDuration(props.duration)}</>;
}
