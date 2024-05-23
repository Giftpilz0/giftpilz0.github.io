---
layout: default
title: Git Workflow
parent: Git
---

______________________________________________________________________

In Git, your local repository consists of three main components:

| Component            | Description                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Working Copy         | Contains the actual project files, where you make changes.                                                                      |
| Index (Staging Area) | Acts as an intermediate stage between your working copy and the HEAD (last commit). You use it to prepare changes for a commit. |
| HEAD                 | Points to your last commit, representing the current state of your project.                                                     |

![Git Workflow](/img/git_workflow.png)

______________________________________________________________________

# Breakdown of the typical Git workflow:

### Add Changes to the Index

To include your changes in the next commit:

```
git add <file>
```

### Commit Your Changes

Once you've added changes to the index, commit them with a meaningful message:

```
git commit -m "Your commit message here"
```

### Upload Changes to a Remote Repository

To upload your local commits to a remote repository:

```
git push origin main
```

This command pushes your changes to the `main` branch of the remote repository `origin`.

### General Git Workflow:

Here's a general workflow for working with Git branches:

```
# Create and switch to a new branch
git checkout -b FeatureBranch

# Add all changes in the working directory to the index
git add .

# Commit your changes with a descriptive message
git commit -m 'Your changelog message here'

# If needed, perform an interactive rebase to refine commit history
git rebase -i

# Switch back to the main branch
git checkout main

# Merge the feature branch into the main branch
git merge FeatureBranch

# Delete the feature branch (if you no longer need it)
git branch -d FeatureBranch
```
