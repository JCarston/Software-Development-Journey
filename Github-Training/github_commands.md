## <u>**Configuration Commands:**</u>
### git config --global user.name "[name]" 
    - Sets the name you want on your commits
### git config --global user.email "[email]"
    - Sets the email you want on your commits
### git config --global color.ui auto
    - Enables helpful colors for the CLI output

## <u>**Creating Repositories:**</u>
### git init
    - Turn an existing directory into a git repository
### git clone [url]
    - Downloads a repository that already exists within GitHub


## <u>**Branches:**</u>
### git branch [branch-name]
    - Creates a new branch. 
    - Can clone from existing branch.
### git checkout [branch-name]
    - Switches to the specified branch and updates working directory
### git merge
    - Combines the specific branche's history into the current branch
    - This is usally done in pull request
### git branch -d [branch-name]
    - Deletes the specified branch
## git branch-m [branchname]
    - Rename branch. You much be inside the branch you want to rename.
### git branch --list
    - Show list of all branches in repo
### git switch [branch-name]
    - Changes to the branch specified.

## <u>**Synchronize Changes:**</u>
### git fetch (Everything gets pulled down remote/Github to local)
    - Downloads all history from the remote branches
### git merge
    - Combines the specific branche's history into the current branch
    - This is usally done in pull request
### git push (local to remote/Github)
    - Uploads all local branch commits to GitHub
### git pull (remote/Github to local)
    - Updates your current local working branch with all new commits from the remote branch
    - Combination of git fetch and git merge


## <u>**Browse and inspect repo over time:**</u>
### git log
    - Lists version history for the current branch
### git log --follow [file]
    - Lists version history for a file (including renames).
### git diff [first-branch] [second-branch]
    - Shows context difference between two branches
### git show [commit]
    - Output metadata and content change of the specified commit
### git add [filename]
    - Snapshots the file in preparation for versioning
### git commit -m "[descriptive message]"
    - Records file snapshots permantely in version history
### git status
    - Shows current status of the repo and where you are at.

## <u>**General Command walkthrough:**</u>
    - Make file changes
    - git add [filename or .]
        - (Period selects all files)
    - git commit -m "[descriptive message]" 
        - (Local to remote branch)
    - git push origin [branch]
        - (Local to remote branch)
    - git switch [branch_name]
    - git pull origin [branch_name]
        - (Remote to Local)
    - git push origin [branch_name]
        - (Remote to Remote)

## <u>**The .gitignore file**</u>
    - Exclude files from being tracked with Git

## <u>**Erase mistakes and craft replacement history:**</u>
### git reset [commit]
    - undoes all commits after [commit], preserving changes
### git reset --hard [commit]
    - Discards all history and changes back to the specified commit



## <u>**Resources used:**</u>
    -https://training.github.com/downloads/github-git-cheat-sheet.pdf
    - https://deepnotes.app/pages/nRea-8JgIXvbIyEi0ONCN