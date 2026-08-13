# Add Data to SEAScope

## Data Format

## Download samples
You can download samples from the [SEAScope webpage](https://seascope.oceandatalab.com/data.html)

## Add your samples to SEAScope

### Linux
* Download your samples (`*.tar.gz` archive)
* Uncompress the archive
* Copy the content (the folders and files in the sample data directory) into [workspace]/seascope/data

[How to add data to SEAScope on Linux](https://youtu.be/3ZAzgl3v2lo?si=Mlstme382XVkknAp)

### macOS
* Download your samples (`*.zip` archive)
* Drag-n-drop the zipped or unzipped folder onto the “SEAScope” icon
* Alternatively you can copy the content (the folders and files in the data directory) into ~/SEAScope-workspace/data directory

[How to add data to SEAScope on macOS](https://youtu.be/s5X3ewpmcuw?si=1s4V9qxMoJr8qKPV)

### Windows
* Download your samples (`*.zip` archive)
* Uncompress the archive
* Copy the content (the folders and files in the sample data directory) into [workspace]/seascope/data

[How to add data to SEAScope on Windows](https://youtu.be/TsJSg7V7WNU?si=5F5uN4TEA33it1Ui)

## Index

At startup SEAScope builds/updates an index that lists all the granules available in the `data` directory.
If SEAScope detects a change in the `data` directory, it will ask you whether or not the index should be updated. When prompted, agree to rebuild the index.

Alternatively, you can delete the `[workspace]/seascope/index.fb` file (or `~/SEAScope-workspace/index.fb` on macOS) when SEAScope is not running: the file will be regenerated automatically next time you start the application.
