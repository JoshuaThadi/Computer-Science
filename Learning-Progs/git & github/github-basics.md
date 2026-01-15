# Git & GitHub Commands Guide

This README provides a professional, complete reference for **creating**, **pushing**, **pulling**, **updating**, and **deleting** content using Git and GitHub. It is suitable for beginners and intermediate developers.

---

## Prerequisites

* Git installed: [https://git-scm.com/](https://git-scm.com/)
* GitHub account
* Basic terminal/command prompt knowledge

---

## Initial Git Configuration (One-Time Setup)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Check configuration:

```bash
git config --list
```

---

## Creating a New Repository

### Option 1: Create Locally and Push to GitHub

```bash
mkdir my-project
cd my-project
git init
```

Add files:

```bash
git add .
```

First commit:

```bash
git commit -m "Initial commit"
```

Add GitHub remote:

```bash
git remote add origin https://github.com/username/repository-name.git
```

Push to GitHub:

```bash
git branch -M main
git push -u origin main
```

---

### Option 2: Clone an Existing Repository

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

---

## Basic Git Workflow

### Check Repository Status

```bash
git status
```

### Track Changes

```bash
git add filename
git add .
```

### Commit Changes

```bash
git commit -m "Describe your changes"
```

---

## Push Changes to GitHub

```bash
git push origin main
```

If upstream is already set:

```bash
git push
```

---

## Pull Changes from GitHub

Fetch and merge remote changes:

```bash
git pull origin main
```

---

## Update Code (Edit Existing Files)

```bash
git add .
git commit -m "Updated existing files"
git push
```

---

## Delete Files

### Delete a File Locally and on GitHub

```bash
git rm filename
git commit -m "Removed filename"
git push
```

### Delete a Directory

```bash
git rm -r foldername
git commit -m "Removed folder"
git push
```

---

## Rename Files or Folders

```bash
git mv oldname newname
git commit -m "Renamed file"
git push
```

---

## Branch Management

### Create a New Branch

```bash
git branch branch-name
git checkout branch-name
```

Or:

```bash
git checkout -b branch-name
```

### Push Branch to GitHub

```bash
git push origin branch-name
```

### Switch Branches

```bash
git checkout main
```

### Delete a Branch

Local:

```bash
git branch -d branch-name
```

Remote:

```bash
git push origin --delete branch-name
```

---

## Undo Changes

### Undo Unstaged Changes

```bash
git checkout -- filename
```

### Unstage a File

```bash
git reset filename
```

### Amend Last Commit

```bash
git commit --amend
```

---

## Stashing Changes

Save temporary changes:

```bash
git stash
```

Apply stash:

```bash
git stash pop
```

List stashes:

```bash
git stash list
```

---

## View Commit History

```bash
git log
git log --oneline
```

---

## Sync Forked Repository

```bash
git remote add upstream https://github.com/original-owner/repository.git
git fetch upstream
git merge upstream/main
git push
```

---

## Remove Git Tracking

```bash
rm -rf .git
```

---

## Common GitHub Errors and Fixes

### Authentication Failed

* Use Personal Access Token instead of password

### Push Rejected (Non-fast-forward)

```bash
git pull --rebase
git push
```

---

## Best Practices

* Commit frequently with clear messages
* Pull before pushing
* Use branches for features
* Do not commit secrets or credentials

---

## License

This guide is provided for educational and professional use.
