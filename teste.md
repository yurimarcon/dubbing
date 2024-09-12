[
    {
        "Id": "53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0",
        "Created": "2024-09-12T16:06:37.622135259Z",
        "Path": "flask",
        "Args": [
            "run",
            "--host=0.0.0.0"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 20124,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-09-12T16:06:38.17864076Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:6d6acc86fb1b3e520fca9aad49cb7d4698368959558cd0fd1b2a5d7f6d58e94c",
        "ResolvConfPath": "/var/lib/docker/containers/53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0/hostname",
        "HostsPath": "/var/lib/docker/containers/53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0/hosts",
        "LogPath": "/var/lib/docker/containers/53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0/53cc25313a0d6d27204ef77e8a0d533cd3543479c20d8d22ad0ec6a534e6f1d0-json.log",
        "Name": "/dubbing-web-1",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": [
            "a00bf27782e60c1dead9a612c6ed8368e9a447694466b592aa7b2cc8f08fcf64"
        ],
        "HostConfig": {
            "Binds": [
                "/Users/yurimarcon/Documents/projetos/Dubbing:/app:rw"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "dubbing_default",
            "PortBindings": {
                "5000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5001"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                0,
                0
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": null,
            "DnsOptions": null,
            "DnsSearch": null,
            "ExtraHosts": [],
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 8589934592,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 100000,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": null,
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 4294967296,
            "MemorySwap": 17179869184,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [
                {
                    "Name": "nproc",
                    "Hard": 65535,
                    "Soft": 65535
                },
                {
                    "Name": "nofile",
                    "Hard": 40000,
                    "Soft": 20000
                }
            ],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/7d7fa81ca2e5c7ab8076276219da2d44fe0f8db1625e92cd011033a41378e7ad-init/diff:/var/lib/docker/overlay2/9ilgc5af1pvms2xofs7wx4w7y/diff:/var/lib/docker/overlay2/e9cjjdy4gg82a60o4ya4ng1wp/diff:/var/lib/docker/overlay2/99gzbuowm1soyjpty2kwxdw6x/diff:/var/lib/docker/overlay2/npx44wtw89bdh6mwppnopt4hr/diff:/var/lib/docker/overlay2/34910yfw1uktf9x0bk89wh776/diff:/var/lib/docker/overlay2/pjiuvk60uoj61efq5ku28hskl/diff:/var/lib/docker/overlay2/x3dtn0i6eoymord8vo3sorulg/diff:/var/lib/docker/overlay2/f3jvrqqfqwiyd9du1jr5n44b0/diff:/var/lib/docker/overlay2/r41mt2kpea2001idy3v5clg90/diff:/var/lib/docker/overlay2/gfgt6s6q6hfxe00yzpdut4lb0/diff:/var/lib/docker/overlay2/iowodl05u12q9t0uyic6u4zgs/diff:/var/lib/docker/overlay2/f0906f62b7d30095596e1482b49ff01c8321dead59fc69cb527c3bda81e42e68/diff:/var/lib/docker/overlay2/7104eda7dbc1d7a60214274c95144e24279287d3e0ea802cd95b933e2d48aff8/diff:/var/lib/docker/overlay2/8f581d86aacfcde2b19ca365484fe6a5de53a500c24285bec8e223e442f1d499/diff:/var/lib/docker/overlay2/e27aec51cfa3c0fdfdaa5bbff4b801c793ed3689e85bab580bbee95af674f11e/diff:/var/lib/docker/overlay2/8f94f17e6434dde047f9988d487225f35152e0ccd33617195f2e1a70555aba51/diff",
                "MergedDir": "/var/lib/docker/overlay2/7d7fa81ca2e5c7ab8076276219da2d44fe0f8db1625e92cd011033a41378e7ad/merged",
                "UpperDir": "/var/lib/docker/overlay2/7d7fa81ca2e5c7ab8076276219da2d44fe0f8db1625e92cd011033a41378e7ad/diff",
                "WorkDir": "/var/lib/docker/overlay2/7d7fa81ca2e5c7ab8076276219da2d44fe0f8db1625e92cd011033a41378e7ad/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/Users/yurimarcon/Documents/projetos/Dubbing",
                "Destination": "/app",
                "Mode": "rw",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "53cc25313a0d",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "5000/tcp": {},
                "5555/tcp": {},
                "6379/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "FLASK_APP=app.py",
                "FLASK_ENV=development",
                "PATH=/root/.cargo/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.10",
                "PYTHON_PIP_VERSION=24.0",
                "PYTHON_SETUPTOOLS_VERSION=65.5.1",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/def4aec84b261b939137dd1c69eff0aabb4a7bf4/public/get-pip.py",
                "PYTHON_GET_PIP_SHA256=bc37786ec99618416cc0a0ca32833da447f4d91ab51d2c138dd15b7af21e8e9a"
            ],
            "Cmd": [
                "flask",
                "run",
                "--host=0.0.0.0"
            ],
            "Image": "dubbing-web",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "com.docker.compose.config-hash": "9e359bc849a0c362cfc17ad10b99828503ea0e93ea4cf72d59bb75137e13e709",
                "com.docker.compose.container-number": "1",
                "com.docker.compose.depends_on": "redis:service_started:false",
                "com.docker.compose.image": "sha256:6d6acc86fb1b3e520fca9aad49cb7d4698368959558cd0fd1b2a5d7f6d58e94c",
                "com.docker.compose.oneoff": "False",
                "com.docker.compose.project": "dubbing",
                "com.docker.compose.project.config_files": "/Users/yurimarcon/Documents/projetos/Dubbing/docker-compose.yml",
                "com.docker.compose.project.working_dir": "/Users/yurimarcon/Documents/projetos/Dubbing",
                "com.docker.compose.service": "web",
                "com.docker.compose.version": "2.27.1"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "26bd16b9539e77ba521609b04fe472028eb8cc3a7286c489a6ccf09842f5a8b1",
            "SandboxKey": "/var/run/docker/netns/26bd16b9539e",
            "Ports": {
                "5000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5001"
                    }
                ],
                "5555/tcp": null,
                "6379/tcp": null
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "dubbing_default": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "dubbing-web-1",
                        "web"
                    ],
                    "MacAddress": "02:42:ac:1b:00:04",
                    "NetworkID": "acc430d8b3ebe86cfafaacf7f8fa9d61ff086666176432e6de615c8d2fb33759",
                    "EndpointID": "9c37b8dbbfc9162ec2fbe2e0341ab47fb3f482f0c502e354fbe467c688f0c028",
                    "Gateway": "172.27.0.1",
                    "IPAddress": "172.27.0.4",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DriverOpts": null,
                    "DNSNames": [
                        "dubbing-web-1",
                        "web",
                        "53cc25313a0d"
                    ]
                }
            }
        }
    }
]
