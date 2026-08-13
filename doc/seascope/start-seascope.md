# Starting SEAScope

## Open SEAScope Viewer

### Linux

In the file explorer:

* open the [workspace]/seascope directory
* double-click on SEAScope icon

OR

In a shell:

```bash
> cd [workspace]/seascope
> ./seascope
```

### macOS

Open SEAScope like you do any other application

### Windows

In the file explorer:

* open the [workspace]/seascope directory
* double-click on SEAScope icon

## How SEAScope works

The first time SEAScope is started, the application creates a configuration file named `config.ini` that contains paths for the colormaps, data, plugins,… directories.

The `data` directory will have one subdirectory for each collection:
it contains one or several granules. A configuration file is provided to define
how SEAScope should render these granules. The `[subdirectory].ini` file has the same name as the subdirectory it relates to. Old configuration file could be provided in the subdirectory itself and are named `config.ini`.
At startup SEAScope will also create an index for all the compatible granules
found in the data directory (if it exists):
this index will contain the full path for each file that SEAScope is able to load.

> [!NOTE]
> If you decide to move the seascope directory somewhere else, make sure to delete the seascope/config.ini and seascope/index.fb files because they will still contain references to the old location. SEAScope will recreate them for you the next time you start the application.
