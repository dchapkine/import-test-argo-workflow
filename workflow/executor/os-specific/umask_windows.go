package os_specific

import "syscall"

func AllowGrantingAccessToEveryone() {
	// There's no umask in Windows.
	// TODO: figure out how we can allow this in Windows.
}
