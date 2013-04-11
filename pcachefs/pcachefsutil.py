# Utility methods used across pcachefs
import errno

DEBUG = True
def debug(*s):
	if DEBUG:
		print s

# Error codes
# source: /usr/lib/syslinux/com32/include/errno.h
E_NO_SUCH_FILE = -errno.ENOENT
E_NOT_PERMITTED = -errno.EPERM
E_IO_ERROR = -errno.EIO
E_PERM_DENIED = -errno.EACCES
E_READ_ONLY = -errno.EROFS
E_NOT_IMPL= -errno.ENOSYS
E_INVALID_ARG = -errno.EINVAL

