---
title: "Create personal website using MD on GitHub note"
date: 2026-09-20
authors:
  - name: Charlih Chen
    email: charlih_chen@hotmail.com
    orcid: 0000-0001-5437-4073
    url: https://charlih.com
description: Create personal website using MD on GitHub note.
thumbnail: https://charlih.com/thumbnail/thumbnail1.jpg
tags:
  - MyST Markdown
  - GitHub Note
  - GitHub Actions
  - Personal website
keywords:
  - MyST Markdown
  - GitHub Note
  - GitHub Actions
  - Personal website
---

# Create personal website using MD on GitHub note

## Q1: The custom domain via CNAME is not working even updated the DNS on purchased provider?

## A1: 

If you configure a custom domain (via CNAME), remove AKA using # to mark the BASE_URL environment variable from deploy.yml 

charlihchen/charlih/CNAME : charlih.com

charlihchen/charlih/.gitHub/workflows/deploy.yml

```diff
.....
      - name: Build HTML Assets
        # Remove BASE_URL if using a custom domain (CNAME)
-       # env:
-        # BASE_URL: /${{ github.event.repository.name }}
        run: myst build --html
.....
```

## Q2: Why there is no Banner, Primary Sidebar, Secondary Sidebar, Website Header, Website Footer section areas?
## A2:

Have to enable the personal website repository on GitHub from "**Settings**" >> "**Pages**" >> select "**GitHub Actions**" under "Build and deployment" section

"**Re-run jobs**" from deploy shows in red color. To fix all error and "**Re-run job**" till no error email to you.
