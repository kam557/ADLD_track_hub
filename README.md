# How to update this track hub

## Software requirements

- [pixi](https://pixi.prefix.dev/latest/) (will install other dependecies for building this project)
- [direnv](https://pixi.prefix.dev/latest/integration/third_party/direnv/) (mainly a convenience to automatically activate the dev environment)
- Microsoft Excel (for updating extended data)
- [git](https://git-scm.com/) (to clone this repo and push updates)
- this cloned repo

We can then rebuild the working environment from these dependencies and automatically activate it by just enteringt the directory.

Clone this repo with the following command:
```bash
git clone https://github.com/tshanebuckley/ADLD_track_hub.git
```

Enter the repository directory:
```bash
cd ADLD_track_hub
```

Initialize direnv:
```bash
direnv allow
```

Install our pixi-managed dependencies:
```bash
task sync
```

NOTE => if you forget the exact command in this environment, you can find them with:
```
task --list
```

## General Principle: Merging by Ids

Really, all this does is a few merges by lane IDs from the bed file pulled from the working version of the UCSC genome browser and an excel file with tables where each track id should be implemented as a `Item name`. We are then using this merged data to create an extended bigBed file that contains annotations on how to display this data (this is handled for you in the python code in this repo, so no need to worry about the specifics for just updating data).

### 1. Update the UCSC track hub

Go to the custom tracks that have been implemented on the UCSC genome browser as the working version of the lanes for this track hub. Update them accordingly. You may be able to skip this step of you are manually editing the bed file that would be uploaded to the genome browser. The updated version of this file should be placed at `data/data.bed`.

### 2. Update the excel file

This file is located at `data/data.xlsx`. Just update the 3 sheets in this file to include the new data by adding new rows and/or updating previous rows. If new data points are to be added, this goes into updating the python code and is beyond this basic tutorial.

### 3. Run the build command

This just runs the python code for you that automated a bunch of small updates across files and build the updated track hub into the `hub` folder. Note here that the `data` folder is our raw data and the `hub` folder is that data reorganized so that it can be read by the UCSC genome browser.

```bash
task build
```
...and check that updates have been made...
```bash
git status
```

### 4. Push the updates (this is a normal git flow)
From the root of this directory (the `ADLD_track_hub` folder):
```bash
# This tells git to choose all our edited files for 
git add .
```

Now we add a "commit", or save our changes:
```bash
# Note that you should provide a small message that explains the work done
git commit -m "my updates"
```

Finally, push the updates to GitHub:
```bash
git push
```

After this, the data should be viewable on GitHub and should automatically update on the UCSC genome browser so long as you have already registered the track hub. However, the UCSC genome browser updates vary in how long until they are viewable and sometimes require clearing your cache to clear the old version. To clear the cache, click the `Reset All User Settings` button in the UCSC genome browser menu.

### 5. Follow the following UCSC documentation to register this track hub

In the UCSC genome browser main menu click `Track Hubs` under `My Data`. For this repo, you will give the following URL for the `URL` input: 
```bash
https://raw.githubusercontent.com/tshanebuckley/ADLD_track_hub/master/hub/hub.txt
```

Note that accessing raw files from GitHub programmatically is generally formatted in the following manner:
```bash
https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path_to_file}
```

Finally, hit the `Add Hub` button. You can now integrate this custom track hub into a public session to share it.
