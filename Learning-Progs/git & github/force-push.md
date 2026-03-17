## 1️⃣ Go to your folder

```bash
cd C:\Users\Joshua\Downloads\Void-OSE
```

---

## 2️⃣ Initialize Git (if not already)

```bash
git init
```

---

## 3️⃣ Add your GitHub repo as remote

```bash
git remote add origin https://github.com/username/githubrepo.git
```

---

## 4️⃣ Add all files

```bash
git add .
```

---

## 5️⃣ Commit

```bash
git commit -m "Initial commit - Void OSE project"
```

---

## 6️⃣ Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

# ⚠️ If repo already has files (IMPORTANT)

If your GitHub repo is **not empty**, do this instead:

```bash
git pull origin main --rebase
git push origin main
```

---

# 🔥 If you get conflict errors (like before)

Just force push (fastest solution):

```bash
git push -f origin main
```
