<div align="center">

# Asrın Kılıç

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=C23B3B&center=true&vCenter=true&width=560&lines=Building+production+systems+solo;FastAPI+%2B+Next.js+%2B+PostgreSQL;AI+tooling+%26+model+orchestration;Currently+running+a+one-person+VDS" alt="Typing SVG" />

<br/>

<a href="https://dxtl.com.tr"><img src="https://img.shields.io/static/v1?label=&message=Portfolio&color=0a0a0f&style=flat-square&logo=firefox&logoColor=C23B3B" /></a>
<a href="mailto:asrinklcc@dxtl.com.tr"><img src="https://img.shields.io/static/v1?label=&message=asrinklcc%40dxtl.com.tr&color=0a0a0f&style=flat-square&logo=gmail&logoColor=C23B3B" /></a>
<a href="https://github.com/dixtuel"><img src="https://img.shields.io/static/v1?label=&message=dixtuel&color=0a0a0f&style=flat-square&logo=github&logoColor=C23B3B" /></a>

<br/>

<img src="https://komarev.com/ghpvc/?username=dixtuel&color=8B0000&style=flat-square&label=Profile+Views" />
<img src="https://img.shields.io/github/followers/dixtuel?style=flat-square&color=8B0000&label=Followers" />

</div>

---

### Hakkımda

Tek başıma kendi sunucumu (VDS) yönetip üzerinde birden fazla production servisi işleten bir full stack geliştiriciyim. İşin "yazılım" kısmı kadar "işletme" kısmıyla da ilgileniyorum: deploy, izleme, güvenlik, yedekleme — hepsi tek elden, tek kişilik bir operasyon.

Backend'de Python (FastAPI, Flask) ve TypeScript (Next.js) kullanıyorum, veriyi PostgreSQL/Redis üzerine kuruyorum. Son dönemde ağırlığı AI destekli developer tooling'e verdim: model orkestrasyonu, tool-calling/agent döngüleri, AI gateway'ler ve otomasyon.

**Açık olduğum konular:** backend/AI tooling projelerinde işbirliği, açık kaynağa katkı, self-hosted altyapı üzerine sohbet.

---

### Teknoloji

Aşağıdaki liste gerçekten kullandığım şeylerden oluşuyor — proje bağımlılık dosyalarından (`pyproject.toml`, `package.json`) ve kaynak kodundan doğrulandı, rastgele doldurulmadı.

**Diller**

<img src="https://skillicons.dev/icons?i=python,ts,js,bash&theme=dark" />

**Frontend**

<img src="https://skillicons.dev/icons?i=nextjs,react,tailwind,html,css&theme=dark" />

**Backend & Veritabanı**

<img src="https://skillicons.dev/icons?i=fastapi,flask,nodejs,express,postgres,sqlite,redis,prisma&theme=dark" />

**Cloud, DevOps & Araçlar**

<img src="https://skillicons.dev/icons?i=docker,cloudflare,linux,git,github,githubactions,vercel,render&theme=dark" />

---

### AI / ML Uzmanlığı

| Alan | Seviye | Detay |
|---|---|---|
| Çoklu-model orkestrasyonu / routing | Production | Mikoshi AI'da 7 görev profiline (chat, reasoning, code, vision, tool_agent vb.) göre model seçimi ve versiyonlu model zinciri yönetimi |
| Native tool calling / ReAct döngüsü | Production | Model `tool_calls` ürettiğinde aracı çalıştırıp sonucu tekrar modele besleyen döngü; allowlist'e girmeyen modellerde fail-closed |
| AI Gateway / provider soyutlama | Production | CloudClaude Workers AI — Anthropic Messages API'yi Workers AI'nin OpenAI-uyumlu endpoint'ine çeviren adaptör, 429 quota'da otomatik provider/model rotasyonu ve dinamik fallback zinciri |
| AI destekli içerik üretimi | Uygulanmış | Commit Günlüğü'nde ham commit/PR verisini müşteri diline çevrilmiş changelog taslağına dönüştüren worker |
| RAG worker altyapısı | Uygulanmış | Mikoshi AI'da ayrı bir Dramatiq kuyruğu (`rag-worker`) olarak çalışıyor |

---

### Öne Çıkan Projeler

<details open>
<summary><b>PulseRoute — Enterprise-Grade URL Shortener, Custom Domains & Real-Time Analytics</b></summary>
<br>

Multi-tenant link kısaltma platformu: sub-10ms yönlendirme, Caddy On-Demand TLS ile özel domain doğrulama, Redis Stream tabanlı non-blocking analitik hattı ve workspace bazlı yetkilendirme.

| | |
|---|---|
| **Stack** | FastAPI, SQLAlchemy (async), PostgreSQL/SQLite, Redis, Tailwind CSS + Chart.js (dashboard), Typer + Rich (CLI), Caddy |
| **Ölçek** | Tek instance, self-hosted / Render — çoklu workspace, izole veri modeliyle çok-kiracılı çalışacak şekilde tasarlandı |
| **Performans** | Redis cache-aside + singleflight locking ile sub-10ms HTTP 307 yönlendirme |
| **Güvenlik** | Parametreli sorgular, workspace izolasyonu + auth zorunluluğu, brute-force jail (10 denemede 10dk ban), KVKK/GDPR IP maskeleme, AES-256-GCM veri şifreleme |
| **CI/CD** | GitHub Actions (`ci.yml`, `docker-publish.yml`) |
| **Repo** | [dixtuel/pulseroute](https://github.com/dixtuel/pulseroute) — public, MIT |
| **Demo** | [pulseroute.onrender.com](https://pulseroute.onrender.com) |

</details>

<details>
<summary><b>Commit Günlüğü — White-Label Changelog Widget'ı</b></summary>
<br>

GitHub commit ve pull request'leri okuyup müşteri diline çevrilmiş bir "Yenilikler" bültenine dönüştüren, siteye tek satır script ile gömülen changelog widget'ı ve panosu. Ajans/freelancer'ların birden fazla müşteri projesine white-label changelog kurması hedefleniyor.

| | |
|---|---|
| **Stack** | Next.js 14 (App Router), React, Prisma + PostgreSQL, BullMQ + ioredis (worker kuyruğu), GitHub App (Octokit webhook), NextAuth, Stripe |
| **Ölçek** | Çok-müşterili SaaS olarak tasarlandı; bağımsız, framework'süz gömülebilir widget (esbuild ile derleniyor) |
| **Durum** | Uçtan uca tasarlanmış MVP scaffold — bu ortamda Node.js kurulu olmadığından `npm install`/`next build` henüz doğrulanmadı |
| **Repo** | [dixtuel/commit-gunlugu](https://github.com/dixtuel/commit-gunlugu) — private |

</details>

<details>
<summary><b>CloudClaude Workers AI</b></summary>
<br>

Claude Code'un Anthropic Messages API isteklerini Cloudflare Workers AI'nin OpenAI-uyumlu chat endpoint'ine çeviren, yerel çalışan bağımsız (unofficial) bir adaptör. Dosya/shell gibi araçlar yine yerel makinede çalışır.

| | |
|---|---|
| **Stack** | Node.js, Bash, Cloudflare Workers AI / AI Gateway |
| **Öne çıkan** | Opsiyonel AI Gateway BYOK modu, Workers AI 429 quota'sında otomatik provider/model rotasyonu, dinamik routing ve çok-sağlayıcılı fallback zinciri, sır içermeyen (secret-free) tanılama modu |
| **Kapsam** | Yalnızca `127.0.0.1`'de dinleyen, tek Claude Code oturumu boyunca yaşayan yerel adaptör |
| **Repo** | [dixtuel/cloudclaude-workers-ai](https://github.com/dixtuel/cloudclaude-workers-ai) — private |

</details>

<details>
<summary><b>Mikoshi AI — "Yapay zekânla gerçekten çalış."</b></summary>
<br>

Sohbet, araştırma, dosya analizi ve görsel üretimini tek bir kişisel alanda birleştiren kişisel AI platformu. Web paneli, Telegram/Discord botları ve Home Assistant köprüsünü tek çatı altında toplar.

| | |
|---|---|
| **Stack** | Flask/Gunicorn web paneli, PostgreSQL, Redis + Dramatiq worker kuyrukları (ai/heavy/media/rag) |
| **Öne çıkan** | 7 görev profiline göre çoklu model routing, native tool calling ile ReAct döngüsü (web arama, hava durumu, rota, oyun/anime sorgulama vb.), Telegram/Discord bot entegrasyonu, Home Assistant MQTT köprüsü |
| **Kapsam** | Kapalı kaynak, kişisel altyapıda production'da çalışıyor |

</details>

<details>
<summary><b>Pixel Terzisi — Fotoğraf Restorasyon Servisi</b></summary>
<br>

Fotoğraf restorasyonu, renklendirme ve Photoshop hizmeti sunan, sipariş akışını Shopier'e bağlayan küçük ölçekli e-ticaret sitesi.

| | |
|---|---|
| **Stack** | Node.js/Express backend, statik frontend, Font Awesome, Nginx, Shopier entegrasyonu |
| **Canlı** | [pixel.dxtl.com.tr](https://pixel.dxtl.com.tr) |

</details>

---

### GitHub İstatistikleri

<div align="center">

<img src="https://gh-readme-stats.vercel.app/api?username=dixtuel&show_icons=true&hide_border=true&bg_color=0a0a0f&title_color=C23B3B&icon_color=8B0000&text_color=e5c9c9" width="48%" />
<img src="https://streak-stats.demolab.com/?user=dixtuel&hide_border=true&background=0a0a0f&stroke=8B0000&ring=8B0000&fire=C23B3B&currStreakLabel=e5c9c9&sideLabels=e5c9c9&currStreakNum=e5c9c9&sideNums=e5c9c9&dates=8a7070" width="48%" />

<img src="https://gh-readme-stats.vercel.app/api/top-langs/?username=dixtuel&layout=compact&hide_border=true&bg_color=0a0a0f&title_color=C23B3B&text_color=e5c9c9" width="48%" />

</div>

---

### Trophies

<div align="center">

<img src="https://github-trophies.vercel.app/?username=dixtuel&theme=darkhub&no-frame=true&row=1&column=6&margin-w=8" />

</div>

---

### Katkı Aktivitesi

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=dixtuel&bg_color=0a0a0f&color=e5c9c9&line=8B0000&point=C23B3B&hide_border=true" width="97%" />

</div>

---

### Contribution Snake

<div align="center">

<img src="https://raw.githubusercontent.com/dixtuel/dixtuel/output/snake-dark.svg" width="97%" />

</div>

---

### Şu An

```yaml
şu_an:
  geliştiriyor: [PulseRoute, Commit Günlüğü, Mikoshi AI]
  odak: [AI destekli developer tooling, self-hosted altyapı]
  keşfediyor: [AI Gateway / model fallback mimarileri, agent orkestrasyonu]
  açık: [backend/AI tooling işbirliği, açık kaynak katkısı]
```

---

### İletişim

<div align="center">

<a href="mailto:asrinklcc@dxtl.com.tr"><img src="https://img.shields.io/static/v1?label=&message=Gmail&color=0a0a0f&style=flat-square&logo=gmail&logoColor=C23B3B" /></a>
<a href="https://github.com/dixtuel"><img src="https://img.shields.io/static/v1?label=&message=GitHub&color=0a0a0f&style=flat-square&logo=github&logoColor=C23B3B" /></a>
<a href="https://dxtl.com.tr"><img src="https://img.shields.io/static/v1?label=&message=Portfolio&color=0a0a0f&style=flat-square&logo=firefox&logoColor=C23B3B" /></a>

</div>

---

<div align="center">

*Tek başına kurup, tek başına idame ettiriyor.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B0000,55:3d0a0a,100:000000&height=100&section=footer" width="100%"/>

</div>
