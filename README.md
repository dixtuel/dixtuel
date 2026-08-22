<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0817,50:2d1b4e,100:5b21b6&height=200&section=header&text=Asrın%20Kılıç&fontSize=46&fontColor=e9d5ff&animation=fadeIn&fontAlignY=38&desc=Full%20Stack%20%26%20AI%20Systems%20Developer&descAlignY=58&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=A78BFA&center=true&vCenter=true&width=560&lines=Building+production+systems+solo;FastAPI+%2B+PostgreSQL+%2B+Redis;AI+orchestration+%26+automation;Currently+running+a+one-person+VDS" alt="Typing SVG" />

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-dxtl.com.tr-5b21b6?style=for-the-badge&logo=firefox&logoColor=white)](https://dxtl.com.tr)
[![Gmail](https://img.shields.io/badge/Email-asrinklcc%40dxtl.com.tr-6d28d9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:asrinklcc@dxtl.com.tr)
[![GitHub](https://img.shields.io/badge/GitHub-dixtuel-4c1d95?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dixtuel)

![Profile Views](https://komarev.com/ghpvc/?username=dixtuel&color=8b5cf6&style=flat-square&label=Profile+Views)
![Followers](https://img.shields.io/github/followers/dixtuel?style=flat-square&color=8b5cf6&label=Followers)

</div>

---

### Hakkımda

Tek başıma kendi sunucumu (VDS) yönetip üzerinde birden fazla production servisi işleten bir full stack geliştiriciyim. İşin "yazılım" kısmı kadar "işletme" kısmıyla da ilgileniyorum: deploy, izleme, güvenlik açıkları, yedekleme — hepsi tek elden.

Ağırlıklı olarak Python (FastAPI/Flask) ve Node.js ile backend yazıyorum, PostgreSQL/Redis üzerine kuruyorum, son dönemde de AI destekli araçlar (kod asistanları, otomasyon botları, orkestrasyon sistemleri) üzerine yoğunlaşıyorum.

```yaml
şu_an:
  öğreniyor: [AI agent orkestrasyonu, çok-modelli routing]
  geliştiriyor: [PulseRoute, Mikoshi AI, commit-gunlugu]
  ilgi_alanı: [self-hosting, backend güvenliği, developer tooling]
```

---

### Teknoloji

<div align="center">

![Python](https://img.shields.io/badge/-Python-2d1b4e?style=flat-square&logo=python&logoColor=A78BFA)
![FastAPI](https://img.shields.io/badge/-FastAPI-2d1b4e?style=flat-square&logo=fastapi&logoColor=A78BFA)
![Flask](https://img.shields.io/badge/-Flask-2d1b4e?style=flat-square&logo=flask&logoColor=A78BFA)
![Node.js](https://img.shields.io/badge/-Node.js-2d1b4e?style=flat-square&logo=node.js&logoColor=A78BFA)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-2d1b4e?style=flat-square&logo=postgresql&logoColor=A78BFA)
![Redis](https://img.shields.io/badge/-Redis-2d1b4e?style=flat-square&logo=redis&logoColor=A78BFA)
![Docker](https://img.shields.io/badge/-Docker-2d1b4e?style=flat-square&logo=docker&logoColor=A78BFA)
![Cloudflare](https://img.shields.io/badge/-Cloudflare-2d1b4e?style=flat-square&logo=cloudflare&logoColor=A78BFA)
![Linux](https://img.shields.io/badge/-Linux-2d1b4e?style=flat-square&logo=linux&logoColor=A78BFA)
![Nginx](https://img.shields.io/badge/-Nginx-2d1b4e?style=flat-square&logo=nginx&logoColor=A78BFA)

</div>

---

### Projeler

<details open>
<summary><b>🔗 PulseRoute — Açık Kaynak Link Kısaltma & Analitik Platformu</b></summary>
<br>

Multi-tenant link kısaltma servisi: özel domain doğrulama, geo/device tabanlı yönlendirme, workspace bazlı yetkilendirme ve KVKK/GDPR uyumlu anonim analitik.

| | |
|---|---|
| **Stack** | FastAPI, Neon PostgreSQL, Upstash Redis, Caddy On-Demand TLS |
| **Öne çıkan** | Redis Streams ile analitik hattı, custom domain DNS doğrulama, workspace izolasyonu |
| **Demo** | [pulseroute.onrender.com](https://pulseroute.onrender.com) |
| **Repo** | [dixtuel/pulseroute](https://github.com/dixtuel/pulseroute) — public |

</details>

<details>
<summary><b>💬 commit-gunlugu — Otomatik Changelog Widget'ı</b></summary>
<br>

GitHub commit geçmişini otomatik olarak beyaz etiketli (white-label), gömülebilir bir changelog widget'ına çeviren araç.

| | |
|---|---|
| **Amaç** | Repo commit'lerinden okunabilir, müşteri/kullanıcıya gösterilebilir bir değişiklik günlüğü üretmek |
| **Repo** | [dixtuel/commit-gunlugu](https://github.com/dixtuel/commit-gunlugu) — private |

</details>

<details>
<summary><b>🤖 CloudClaude Workers AI</b></summary>
<br>

Claude Code'u Cloudflare Workers AI üzerinden çalıştırmayı sağlayan yerel uyumluluk (compatibility) adaptörü.

| | |
|---|---|
| **Amaç** | Claude Code CLI'ı, Cloudflare'in model altyapısıyla köprülemek |
| **Repo** | [dixtuel/cloudclaude-workers-ai](https://github.com/dixtuel/cloudclaude-workers-ai) — private |

</details>

<details>
<summary><b>🧠 Mikoshi AI — Kişisel AI Orkestrasyon Sistemi</b></summary>
<br>

Web paneli, Telegram/Discord botları ve Home Assistant köprüsünü tek çatı altında toplayan, çoklu AI modeli arasında görev bazlı yönlendirme yapan kişisel platform.

| | |
|---|---|
| **Stack** | Flask/Gunicorn, PostgreSQL, Redis + Dramatiq worker kuyrukları |
| **Öne çıkan** | 7 görev profiline göre model seçimi, native tool calling ile ReAct döngüsü (web arama, hava durumu, rota, oyun/anime sorgulama vb.) |
| **Not** | Kapalı kaynak, kişisel altyapıda çalışıyor |

</details>

<details>
<summary><b>🖼️ Pixel Terzisi — Fotoğraf Restorasyon Servisi</b></summary>
<br>

Fotoğraf restorasyonu, renklendirme ve Photoshop hizmeti sunan, sipariş akışını Shopier'e bağlayan küçük ölçekli e-ticaret sitesi.

| | |
|---|---|
| **Stack** | Node.js/Express backend, statik frontend, Shopier entegrasyonu |
| **Canlı** | [pixel.dxtl.com.tr](https://pixel.dxtl.com.tr) |

</details>

---

### GitHub İstatistikleri

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=dixtuel&show_icons=true&theme=radical&hide_border=true&bg_color=0f0817&title_color=A78BFA&icon_color=8b5cf6&text_color=c4b5fd" width="48%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=dixtuel&theme=radical&hide_border=true&background=0f0817&stroke=8b5cf6&ring=A78BFA&fire=A78BFA&currStreakLabel=c4b5fd" width="48%" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=dixtuel&theme=react-dark&bg_color=0f0817&color=A78BFA&line=8b5cf6&point=e9d5ff&hide_border=true" width="97%" />

</div>

---

<div align="center">

*Tek başına kurup, tek başına idame ettiriyor.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:5b21b6,50:2d1b4e,100:0f0817&height=100&section=footer" width="100%"/>

</div>
