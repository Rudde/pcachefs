pCacheFS provides a simple caching layer for other filesystems, which can make slow, remote filesystems seem very fast to access. The cache does not disappear when you start/stop pCacheFS or reboot - it is **persistent**.

It is designed for caching large amounts of data on remote filesystems that don't change very much, such as movie/music libraries.

## Key features ##
  * you can choose where to store your persistent cache - local harddisk, ramdisk filesystem, etc
  * cache contents of any other filesystem, whether local or remote (even other FUSE filesystems such as _sshfs_)
  * pCacheFS caches data as it is read, and only the bits that are read

Currently pCacheFS mounts are **read-only** - writes are not supported.

See [Example](Example.md) or [the blog article](http://jonnytyers.wordpress.com/2012/12/16/pcachefs-persistently-caches-other-filesystems/) for usage examples.

## Dependencies ##
pCacheFS requires FUSE and the FUSE Python bindings to be installed on your system.

Ubuntu users should be able to use this command to install:
```
    $ sudo apt-get install fuse python-fuse
```