<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,45:3d0a0a,100:8B0000&height=200&section=header&text=Asr%C4%B1n%20K%C4%B1l%C4%B1%C3%A7&fontSize=46&fontColor=f0d0d0&animation=fadeIn&fontAlignY=38&desc=Full%20Stack%20%26%20AI%20Systems%20Developer&descAlignY=58&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=C23B3B&center=true&vCenter=true&width=560&lines=Building+production+systems+solo;FastAPI+%2B+Next.js+%2B+PostgreSQL;AI+tooling+%26+automation;Currently+running+a+one-person+VDS" alt="Typing SVG" />

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

Tek başıma kendi sunucumu (VDS) yönetip üzerinde birden fazla production servisi işleten bir full stack geliştiriciyim. İşin "yazılım" kısmı kadar "işletme" kısmıyla da ilgileniyorum: deploy, izleme, güvenlik, yedekleme — hepsi tek elden.

Backend'de Python (FastAPI, Flask) ve TypeScript (Next.js) kullanıyorum, veriyi PostgreSQL/Redis üzerine kuruyorum, bunun yanında AI destekli araçlar (kod asistanı entegrasyonları, otomasyon botları, model orkestrasyonu) üzerine çalışıyorum.

```yaml
şu_an:
  geliştiriyor: [PulseRoute, Commit Günlüğü, Mikoshi AI]
  odak: [AI destekli developer tooling, self-hosted altyapı]
  ilgi_alanı: [backend güvenliği, model routing, changelog/dev-tooling ürünleri]
```

---

### Teknoloji

Gerçekten kullandığım stack — proje bağımlılıklarından (`pyproject.toml`, `package.json`) alındı:

<div align="center">

![Python](https://img.shields.io/badge/-Python-0a0a0f?style=flat-square&logo=python&logoColor=C23B3B)
![TypeScript](https://img.shields.io/badge/-TypeScript-0a0a0f?style=flat-square&logo=typescript&logoColor=C23B3B)
![FastAPI](https://img.shields.io/badge/-FastAPI-0a0a0f?style=flat-square&logo=fastapi&logoColor=C23B3B)
![Flask](https://img.shields.io/badge/-Flask-0a0a0f?style=flat-square&logo=flask&logoColor=C23B3B)
![Next.js](https://img.shields.io/badge/-Next.js-0a0a0f?style=flat-square&logo=next.js&logoColor=C23B3B)
![Node.js](https://img.shields.io/badge/-Node.js-0a0a0f?style=flat-square&logo=node.js&logoColor=C23B3B)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-0a0a0f?style=flat-square&logo=postgresql&logoColor=C23B3B)
![Redis](https://img.shields.io/badge/-Redis-0a0a0f?style=flat-square&logo=redis&logoColor=C23B3B)
![Prisma](https://img.shields.io/badge/-Prisma-0a0a0f?style=flat-square&logo=prisma&logoColor=C23B3B)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-0a0a0f?style=flat-square&logo=sqlalchemy&logoColor=C23B3B)
![Docker](https://img.shields.io/badge/-Docker-0a0a0f?style=flat-square&logo=docker&logoColor=C23B3B)
![Caddy](https://img.shields.io/badge/-Caddy-0a0a0f?style=flat-square&logo=caddy&logoColor=C23B3B)
![Cloudflare](https://img.shields.io/badge/-Cloudflare-0a0a0f?style=flat-square&logo=cloudflare&logoColor=C23B3B)
![Linux](https://img.shields.io/badge/-Linux-0a0a0f?style=flat-square&logo=linux&logoColor=C23B3B)

</div>

---

### Projeler

<details open>
<summary><b>PulseRoute — Enterprise-Grade URL Shortener, Custom Domains & Real-Time Analytics</b></summary>
<br>

Multi-tenant link kısaltma platformu: sub-10ms yönlendirme, Caddy On-Demand TLS ile özel domain doğrulama, Redis Stream tabanlı non-blocking analitik hattı ve workspace bazlı yetkilendirme.

| | |
|---|---|
| **Stack** | FastAPI, SQLAlchemy (async), PostgreSQL/SQLite, Redis, Typer + Rich CLI, Caddy |
| **Güvenlik** | Parametreli sorgular (SQLi koruması), workspace izolasyonu, brute-force jail, KVKK/GDPR IP maskeleme, AES-256-GCM veri şifreleme |
| **Deploy** | Zero-config Render (embedded SQLite) → tam Docker Compose (Postgres + Redis + Caddy) |
| **Demo** | [pulseroute.onrender.com](https://pulseroute.onrender.com) |
| **Repo** | [dixtuel/pulseroute](https://github.com/dixtuel/pulseroute) — public, MIT |

</details>

<details>
<summary><b>Commit Günlüğü — White-Label Changelog Widget'ı</b></summary>
<br>

GitHub commit ve pull request'leri okuyup müşteri diline çevrilmiş bir "Yenilikler" bültenine dönüştüren, siteye tek satır script ile gömülen changelog widget'ı ve panosu. Ajans/freelancer'ların birden fazla müşteri projesine white-label changelog kurması hedefleniyor.

| | |
|---|---|
| **Stack** | Next.js 14 (App Router), Prisma + PostgreSQL, BullMQ + ioredis (worker kuyruğu), GitHub App (Octokit webhook), NextAuth, Stripe |
| **Yapı** | Pazarlama sitesi + panel (Next.js), bağımsız gömülebilir widget (esbuild), AI destekli commit → changelog özetleme worker'ı |
| **Durum** | Uçtan uca tasarlanmış MVP scaffold — henüz derleme bu ortamda doğrulanmadı |
| **Repo** | [dixtuel/commit-gunlugu](https://github.com/dixtuel/commit-gunlugu) — private |

</details>

<details>
<summary><b>CloudClaude Workers AI</b></summary>
<br>

Claude Code'un Anthropic Messages API isteklerini Cloudflare Workers AI'nin OpenAI-uyumlu chat endpoint'ine çeviren, yerel çalışan bağımsız (unofficial) bir adaptör. Dosya/shell gibi araçlar yine yerel makinede çalışır.

| | |
|---|---|
| **Amaç** | Claude Code CLI'ı Cloudflare Workers AI modelleriyle köprülemek |
| **Öne çıkan** | Opsiyonel AI Gateway BYOK modu, 429 quota'da otomatik provider/model rotasyonu, dinamik routing ve fallback zinciri desteği |
| **Repo** | [dixtuel/cloudclaude-workers-ai](https://github.com/dixtuel/cloudclaude-workers-ai) — private |

</details>

<details>
<summary><b>Mikoshi AI — "Yapay zekânla gerçekten çalış."</b></summary>
<br>

Sohbet, araştırma, dosya analizi ve görsel üretimini tek bir kişisel alanda birleştiren kişisel AI platformu. Web paneli, Telegram/Discord botları ve Home Assistant köprüsünü tek çatı altında toplar.

| | |
|---|---|
| **Stack** | Flask/Gunicorn web paneli, PostgreSQL, Redis + Dramatiq worker kuyrukları |
| **Öne çıkan** | 7 görev profiline göre (chat, reasoning, code, vision, tool_agent...) çoklu model routing, native tool calling ile ReAct döngüsü (web arama, hava durumu, rota, oyun/anime sorgulama vb.) |
| **Not** | Kapalı kaynak, kişisel altyapıda çalışıyor |

</details>

<details>
<summary><b>Pixel Terzisi — Fotoğraf Restorasyon Servisi</b></summary>
<br>

Fotoğraf restorasyonu, renklendirme ve Photoshop hizmeti sunan, sipariş akışını Shopier'e bağlayan küçük ölçekli e-ticaret sitesi.

| | |
|---|---|
| **Stack** | Node.js/Express backend, statik frontend, Nginx, Shopier entegrasyonu |
| **Canlı** | [pixel.dxtl.com.tr](https://pixel.dxtl.com.tr) |

</details>

---

### GitHub İstatistikleri

<div align="center">

<img src="https://github-readme-stats-mu-steel-28.vercel.app/api?username=dixtuel&show_icons=true&hide_border=true&bg_color=0a0a0f&title_color=C23B3B&icon_color=8B0000&text_color=e5c9c9" width="48%" />
<img src="https://streak-stats.demolab.com/?user=dixtuel&hide_border=true&background=0a0a0f&stroke=8B0000&ring=8B0000&fire=C23B3B&currStreakLabel=e5c9c9&sideLabels=e5c9c9&currStreakNum=e5c9c9&sideNums=e5c9c9&dates=8a7070" width="48%" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=dixtuel&bg_color=0a0a0f&color=e5c9c9&line=8B0000&point=C23B3B&hide_border=true" width="97%" />

</div>

---

<div align="center">

*Tek başına kurup, tek başına idame ettiriyor.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B0000,55:3d0a0a,100:000000&height=100&section=footer" width="100%"/>

</div>
