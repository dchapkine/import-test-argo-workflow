package os_specific

import (
	"os"
	"syscall"
)

func GetOsSignal() os.Signal {
	return syscall.SIGINT
}

func IsSIGCHLD(s os.Signal) bool {
	return false // this does not exist on windows
}

func Kill(pid int, s syscall.Signal) error {
	if pid < 0 {
		pid = -pid // // we cannot kill a negative process on windows
	}
	p, err := os.FindProcess(pid)
	if err != nil {
		return err
	}
	return p.Signal(s)
}
