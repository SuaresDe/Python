# Code Versioning

Code versioning, also known as version control, is the practice of tracking and managing changes to source code over time. It enables developers to collaborate efficiently, maintain a history of changes, and revert to previous versions when needed.

## Why is Code Versioning Important?

- **Collaboration**: Multiple developers can work on the same project without overwriting each other's work.
- **History Tracking**: Keeps a record of changes, who made them, and why.
- **Rollback Ability**: Restores a previous version if something breaks.
- **Branching and Merging**: Allows simultaneous work on features, bug fixes, and different project versions.
- **Backup & Recovery**: Prevents data loss by storing code versions safely.

## Types of Version Control Systems (VCS)

### Local Version Control
A basic system where users manually save different versions of files on their computers.  
**Downside**: Prone to human errors and difficult to track changes systematically.

### Centralized Version Control (CVCS)
A single, central server holds all versioned files, and developers pull and push changes from it.  
**Example**: SVN (Subversion), Perforce  
**Downside**: If the central server fails, all version history may be lost.

### Distributed Version Control (DVCS)
Every developer has a full copy of the repository, allowing offline work and better redundancy.  
**Example**: Git, Mercurial  
**Advantage**: No single point of failure, better branching, and collaboration.

## Git: The Most Popular Version Control System

Git is a distributed version control system (DVCS) that allows efficient code versioning and collaboration.  
GitHub, GitLab, and Bitbucket are popular platforms for managing Git repositories remotely.

### Common Git Commands

#### `git clone`
The `git clone` command is used to copy a remote Git repository to your local machine. It downloads all the files, commits, branches, and repository history, allowing you to work on a local copy of the project.

#### `git commit`
The `git commit` command is used to save changes to a Git repository. Each commit acts like a snapshot of your project at a specific point in time, allowing you to track changes and revert if necessary.

#### `git pull`
The `git pull` command is used to update your local repository with the latest changes from a remote repository. It fetches changes and merges them into your current branch automatically.

#### `git push`
The `git push` command uploads committed changes from your local repository to a remote repository (such as GitHub, GitLab, or Bitbucket). This is how you share your work with others or back it up in a remote location.

#### `git config --global credential.helper store or cache`
In Git, when interacting with remote repositories (like GitHub, GitLab, or Bitbucket) over HTTPS, Git asks for authentication (username/password or personal access token). Since repeatedly entering credentials is inconvenient, Git provides credential helpers to store passwords securely.

## GitHub

### What is GitHub?
GitHub is a web-based platform that helps developers store, manage, and collaborate on projects using Git, a version control system. It allows developers to work together on code by tracking changes, merging updates, and maintaining repositories.

## Git Commands Cheat Sheet

### Create or Clone Repositories
```sh
# Clone an existing repository
git clone ssh://user@domain.com/repo.git

# Create a new local repository
git init
```

### Local Changes
```sh
# Check changed files in your working directory
git status

# Show changes to tracked files
git diff

# Add all current changes to the next commit
git add .

# Add some changes in <file> to the next commit
git add -p <file>

# Commit all local changes in tracked files
git commit -a

# Commit previously staged changes
git commit

# Change the last commit (Don't amend published commits!)
git commit --amend
```

### Branches & Tags
```sh
# List all existing branches
git branch -av

# Switch HEAD branch
git switch <branch>

# Create a new branch based on your current HEAD
git branch <new-branch>

# Create a new tracking branch based on a remote branch
git checkout --track <remote/branch>

# Delete a local branch
git branch -d <branch>

# Mark the current commit with a tag
git tag <tag-name>
```

### Commit History
```sh
# Show all commits, starting with newest
git log

# Show changes over time for a specific file
git log -p <file>

# Show who changed what and when in <file>
git blame <file>
```

### Update & Publish
```sh
# List all currently configured remotes
git remote -v

# Show information about a remote
git remote show <remote>

# Add a new remote repository, named <remote>
git remote add <shortname> <url>

# Download all changes from <remote>, but don’t integrate into HEAD
git fetch <remote>

# Download changes and directly merge/integrate into HEAD
git pull <remote> <branch>

# Publish local changes on a remote
git push <remote> <branch>

# Delete a branch on the remote
git push <remote> --delete <branch>

# Publish your tags
git push --tags
```

### Merge & Rebase
```sh
# Merge <branch> into your current HEAD
git merge <branch>

# Rebase your current HEAD onto <branch> (Don't rebase published commits!)
git rebase <branch>

# Abort a rebase
git rebase --abort

# Continue a rebase after resolving conflicts
git rebase --continue

# Use your configured merge tool to solve conflicts
git mergetool

# Use your editor to manually solve conflicts and mark file as resolved
git add <resolved-file>
git rm <resolved-file>
```

### Undo Changes
```sh
# Discard all local changes in your working directory
git reset --hard HEAD

# Discard local changes in a specific file
git checkout HEAD <file>

# Revert a commit (by producing a new commit with contrary changes)
git revert <commit>

# Reset your HEAD pointer to a previous commit and discard all changes since then
git reset --hard <commit>

# Reset but preserve all changes as unstaged changes
git reset <commit>

# Reset but preserve uncommitted local changes
git reset --keep <commit>
```

---
