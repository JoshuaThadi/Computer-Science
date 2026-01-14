## LESSION 1

### step 1: Create a repo in Github and Github folder in local machine

### step 2: Clone the repo in IDE of terminal

**→ git clone [git@github.com](mailto:git@github.com):JoshuaThadi/Demo-Repo.git**

this command will clone the repository from the github to the local machine.

Run the following command in PowerShell to mark the directory as safe:

**→ git config --global --add safe.directory "F:/git & github/Demo-Repo2"**

---

### step 3: Change directory in IDE of github folder
**→ cd Demo-Repo**
this will go from github folder to the demo-repo folder.

---

### step 4: lists all files, including hidden ones
**→ Get-ChildItem -Force 0r** Get-ChildItem -Force | Format-List

---

### step 5: Check the status of the repo
**→  git status**

to check the modified and untracked files, 
The `git status` command shows the **current state of the working directory and staging area**.

---

### step 6: Adding all new, modified files and Tracking deleted files
**→ git add .**
This command stages **all changes** (new, modified, and deleted files) in the current directory and its subdirectories, preparing them for the next commit.

- `git add` → Adds files to the staging area.
- `.` → Represents the **current directory**, meaning it includes all changes in the repository.
- `git add -A` → Stages all changes (same as `git add .` but works from any location in the repo).
- `git add -u` → Stages only modified and deleted files (ignores untracked files).

---

### step 7: check the status again
**→ git status**

---

If You're seeing error because Git doesn't know your identity (name and email), which is required to commit changes.

**Solution: Set Your Git Identity**

Run the following commands in **PowerShell** (replacing with your actual details):

**→ git config --global [user.name](http://user.name/) "Joshua Thadi"
→ git config --global user.email "[your-email@example.com](mailto:your-email@example.com)"**

If you want to set it **only for this repository**, remove `--global`:
**→ git config --local [user.name](http://user.name/) "John Doe"
→ git config --local user.email "[your-email@example.com](mailto:your-email@example.com)"**

**Verify Your Configuration:**

To check if Git has stored your details correctly, run:
**→ git config --global --list**

or for the local repo:
**→ git config --local --list**

Once configured.

If you want to **remove** the globally set Git user name and email, you can use the following commands:
**→ git config --global --unset [user.name](http://user.name/)
→ git config --global --unset user.email**

After running the above commands, check if the values are removed:
**→ git config --global --list**

---

### step 8: Creates a commit (snapshot of changes) and Specifies the commit message in quotes.
**→ git commit -m "Your commit message"**
The `git commit -m` command is used to **save staged changes** in Git with a commit message.

for title and discription:
**→ git commit -m "Added index.html file" -m "demo index.html file for testing”**

it is saved locally, not live in github yet.

---

### **step 9: Push the changes in github repository**

you **do not** need an SSH key if you cloned your repository using **HTTP**. You can push changes using your GitHub **username and password** (or a **personal access token** if required by GitHub).

Since you cloned with HTTP, you can push changes normally using:
**→ git push origin master**

Git now uses **`main`** instead of `master` by default. To check your branch name, run:
**→ git branch**

If you see **`main`** instead of `master`, push using:
**→ git push origin main**

If you haven't committed anything yet, Git won’t recognize the branch. 

Ensure You Have Made a Commit.

ex: 

**→ git add .
→ git commit -m "Initial commit"
→ git push origin main**

---

## LESSION 2

Creating a repository locally and publishing on github.

### step 1: Initialize a new repository

Initialize a new repository by creating a directory locally:
**→ mkdir my-project
→ cd my-project**

The `git init` command initializes a **new Git repository** in a directory. It sets up the necessary Git files to start tracking changes.
**→ git init**
his creates a **`.git`** folder inside the current directory, marking it as a Git repository.

---

### step 2: Check the status
**→ git status**

---

### step 3: Stages a file for commit.
The command `git add README.md` is used to **stage** the `README.md` file so it can be committed to the Git repository.
**→ git add README.md**

---

### step 4: commit message
**→ git commit -m "Created README" -m "description section is empty”**

### step 5: Create a repository in github with the same name as created in local IDE or terminal

run this command:
**→ git remote add origin https://github.com/JoshuaThadi/Demo-Repo2.git**

**links your local Git repository** to the remote repository on GitHub (`Demo-Repo2`).
After adding the remote, push your code using:
**→ git push -u origin main**

---

## Git Brancing

### **Common Git Branch Commands**

### **1. Check Current Branch**

```bash
git branch
```

✔ Lists all local branches and highlights the current one.

### **2. Create a New Branch**

```bash
git branch new-feature
```

✔ Creates a new branch named `new-feature`.

### **3. Switch to a Branch**

```bash
git checkout new-feature
```

or

```bash
git switch new-feature
```

✔ Moves to the `new-feature` branch.

### **4. Create and Switch to a New Branch**

```bash
git checkout -b new-feature
```

or

```bash
git switch -c new-feature
```

✔ Creates and moves to `new-feature` in one step.

### **5. Merge a Branch Into `main`**

```bash
git checkout main
git merge new-feature
```

✔ Merges `new-feature` into `main`.

### **6. Delete a Branch (After Merging)**

```bash
git branch -d new-feature
```

✔ Deletes `new-feature` locally.

### **7. Delete a Remote Branch**

```bash
git push origin --delete new-feature
```

✔ Removes `new-feature` from the remote repository.

### step 1: switching to new branch
**→ git checkout -b feature-readme-instructions**
**→ git branch**

to check the branch exists or not
**→ git checkout main**

to switch to main branch
**→  git add [README.md](http://readme.md/)**

make changes in [readme.md](http://readme.md) file
**→  git commit -m "updated readme”**

commit the message

### Git Commands Documentation

1. Checkout to Main Branch

```
→ git checkout main
```

Description:

Switches the current branch to `main`. This is typically used to return to the main development branch before merging or pulling changes.

---

2. View Differences Between Branches

```
→ git diff feature-readme-instructions
```

Description:

Displays the differences between the current branch and `feature-readme-instructions`. It helps in reviewing what changes exist before merging or committing.

---

3. Check the Status of the Repository

```
→ git status
```

Description:

Shows the current status of the working directory and staging area, including any changes that need to be committed, staged, or pushed.

---

4. Push Changes and Set Upstream

```
→ git push --set-upstream origin feature-readme-instructions
```

Description:

Pushes the `feature-readme-instructions` branch to the remote repository and sets it as the upstream branch, so future `git push` and `git pull` commands automatically use this remote branch.

---

5. Switch Back to the Main Branch

```
→ git checkout main
```

Description:

Moves back to the `main` branch after working on another branch.

---

6. Pull Latest Changes from Remote

```
→ git pull
```

Description:

Fetches and merges the latest changes from the remote repository into the current branch.

---

7. Delete a Local Branch

```
→ git branch -d feature-readme-instructions
```

Description:

Deletes the local branch `feature-readme-instructions` after it has been merged. If the branch contains unmerged changes, use `git branch -D` instead.

---

8. View Differences Between Current Branch and Main

```
→ git diff main
```

Description:

Compares the differences between the current branch and the `main` branch to see what changes have been made.

---

9. Merge the Main Branch into the Current Branch

```
→ git merge main
```

Description:

Merges the latest changes from `main` into the current branch, incorporating any updates before further development or resolving conflicts.

---

**Conclusion**

These Git commands are essential for managing branches, tracking changes, and collaborating on projects efficiently. Always ensure your branch is up-to-date before pushing or merging to avoid conflicts.