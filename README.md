<!-- ═══════════════════════════ HEADER ═══════════════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Pasindu%20Fernando&fontSize=60&fontColor=ffffff&fontAlignY=36&desc=Software%20Engineer%20%40%20Choreo%20Labs%20%E2%80%A2%20Backend%20Nerd&descAlignY=58&descSize=18&animation=fadeIn" width="100%" alt="header" />
</p>

<p align="center">
  <a href="https://github.com/pasindufernando1">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=800&color=36BCF7&center=true&vCenter=true&width=600&lines=Hello+%F0%9F%91%8B+I'm+Pasindu+Fernando;Software+Engineer+%40+Choreo+Labs+%F0%9F%92%BC;Backend+Enthusiast+%E2%9A%99%EF%B8%8F;Always+building%2C+always+learning+%F0%9F%9A%80" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/pasindufdo/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/pasindufernando1"><img src="https://img.shields.io/github/followers/pasindufernando1?label=Followers&style=for-the-badge&logo=github&color=181717" alt="GitHub followers" /></a>
  <img src="https://komarev.com/ghpvc/?username=pasindufernando1&style=for-the-badge&color=36BCF7&label=Profile+Views" alt="Profile views" />
</p>

<!-- ═══════════════════════════ ABOUT ═══════════════════════════ -->
## <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28" alt="wave" /> About Me

<table>
<tr>
<td width="60%" valign="top">

- 💼 **Software Engineer** at **Choreo Labs**
- 🎓 **Computer Science (Hons)** graduate — **UCSC**
- ✨ Top performer of my university batch — **GPA 3.98 / 4.00**
- ⚙️ Backend nerd who loves designing clean, scalable systems
- 🔬 Final-year research deep in virtualization — **KVM / QEMU**
- 🔭 Building developer tooling — contributor to the **Ballerina Language Server** & **Ballerina VS Code extension**
- 🎾 Off the keyboard: volunteer, tennis player & carrom player

</td>
<td width="40%" align="center" valign="middle">

<img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="100%" alt="coding" />

</td>
</tr>
</table>

```go
type Engineer struct {
    Name     string
    Role     string
    Company  string
    Loves    []string
}

me := Engineer{
    Name:    "Pasindu Fernando",
    Role:    "Software Engineer",
    Company: "Choreo Labs",
    Loves:   []string{"Backend Systems", "Algorithms", "Tennis 🎾"},
}
```

<!-- ═══════════════════════════ RESEARCH ═══════════════════════════ -->
## 🔬 Research Spotlight

<table>
<tr>
<td>

### 🧠 Enhancing System Checkpoints for Seamless Fault-Tolerant Live Virtual Machine Migration

<sub>🎓 BSc (Hons) in Computer Science — Undergraduate Thesis · University of Colombo School of Computing · June 2025</sub>

Fault-tolerant live VM migration relies on **incremental checkpointing**: after the first round, only the memory pages that changed are copied to the checkpoint store. My research makes this capture **finer-grained and lighter** using two approaches:

- 🧩 **Mem-Finer:** a model that sends only the *modified bytes inside a page* instead of the whole 4 KB page
- 🗜️ **Lossless compression:** compressing modified pages with **Gzip, LZ4 and Zstd** before they're sent to the checkpoint store

| Technique | Page content reduction |
|:--|:--:|
| 🧩 Mem-Finer | **51 – 69 %** |
| ⚡ LZ4 | **69 – 72 %** |
| 📦 Gzip | **78 – 79 %** |
| 🔹 Zstd | **50 – 52 %** |

> 🏁 **Mem-Finer** and **LZ4** performed best overall, with migration time, downtime, replication, performance and recovery overheads **similar to or lower than the baseline**.

<img src="https://img.shields.io/badge/KVM-CC0000?style=flat-square&logo=linux&logoColor=white" alt="KVM" /> <img src="https://img.shields.io/badge/QEMU-FF6600?style=flat-square&logo=qemu&logoColor=white" alt="QEMU" /> <img src="https://img.shields.io/badge/Live_Migration-4B32C3?style=flat-square" alt="Live Migration" /> <img src="https://img.shields.io/badge/Fault_Tolerance-2E7D32?style=flat-square" alt="Fault Tolerance" /> <img src="https://img.shields.io/badge/Checkpointing-0F766E?style=flat-square" alt="Checkpointing" /> <img src="https://img.shields.io/badge/Compression-6D28D9?style=flat-square" alt="Compression" />

<a href="https://dl.ucsc.cmb.ac.lk/jspui/handle/123456789/4918"><img src="https://img.shields.io/badge/📄_Read_the_thesis-UCSC_Digital_Library-36BCF7?style=for-the-badge&labelColor=1a1b27" alt="Read the thesis" /></a>

</td>
</tr>
</table>

<!-- ═══════════════════════════ OPEN SOURCE ═══════════════════════════ -->
## 🌍 Open Source Contributions

<p>I help build the developer tooling behind <b>Ballerina</b> and <b>WSO2 Integrator</b>: the language server, the VS Code experience and the docs developers use every day.</p>

<table>
<tr>
<td align="center" width="50%">
  <a href="https://github.com/ballerina-platform/ballerina-language-server"><img src="https://github-readme-stats.vercel.app/api/pin/?username=ballerina-platform&repo=ballerina-language-server&theme=tokyonight&hide_border=true&description_lines_count=2" alt="ballerina-language-server" /></a>
  <br/>
  <a href="https://github.com/ballerina-platform/ballerina-language-server/pulls?q=is%3Apr%20is%3Amerged%20author%3Apasindufernando1"><img src="https://img.shields.io/github/issues-search?query=repo%3Aballerina-platform/ballerina-language-server%20is%3Apr%20is%3Amerged%20author%3Apasindufernando1&label=merged%20PRs&style=for-the-badge&color=36BCF7&labelColor=1a1b27" alt="merged PRs" /></a>
</td>
<td align="center" width="50%">
  <a href="https://github.com/ballerina-platform/ballerina-vscode"><img src="https://github-readme-stats.vercel.app/api/pin/?username=ballerina-platform&repo=ballerina-vscode&theme=tokyonight&hide_border=true&description_lines_count=2" alt="ballerina-vscode" /></a>
  <br/>
  <a href="https://github.com/ballerina-platform/ballerina-vscode/pulls?q=is%3Apr%20is%3Amerged%20author%3Apasindufernando1"><img src="https://img.shields.io/github/issues-search?query=repo%3Aballerina-platform/ballerina-vscode%20is%3Apr%20is%3Amerged%20author%3Apasindufernando1&label=merged%20PRs&style=for-the-badge&color=36BCF7&labelColor=1a1b27" alt="merged PRs" /></a>
</td>
</tr>
<tr>
<td align="center" width="50%">
  <a href="https://github.com/wso2/docs-integrator"><img src="https://github-readme-stats.vercel.app/api/pin/?username=wso2&repo=docs-integrator&theme=tokyonight&hide_border=true&description_lines_count=2" alt="docs-integrator" /></a>
  <br/>
  <a href="https://github.com/wso2/docs-integrator/pulls?q=is%3Apr%20is%3Amerged%20author%3Apasindufernando1"><img src="https://img.shields.io/github/issues-search?query=repo%3Awso2/docs-integrator%20is%3Apr%20is%3Amerged%20author%3Apasindufernando1&label=merged%20PRs&style=for-the-badge&color=36BCF7&labelColor=1a1b27" alt="merged PRs" /></a>
</td>
<td align="center" width="50%">
  <a href="https://github.com/wso2/vscode-extensions"><img src="https://github-readme-stats.vercel.app/api/pin/?username=wso2&repo=vscode-extensions&theme=tokyonight&hide_border=true&description_lines_count=2" alt="vscode-extensions" /></a>
  <br/>
  <a href="https://github.com/wso2/vscode-extensions/pulls?q=is%3Apr%20is%3Amerged%20author%3Apasindufernando1"><img src="https://img.shields.io/github/issues-search?query=repo%3Awso2/vscode-extensions%20is%3Apr%20is%3Amerged%20author%3Apasindufernando1&label=merged%20PRs&style=for-the-badge&color=36BCF7&labelColor=1a1b27" alt="merged PRs" /></a>
</td>
</tr>
</table>

<!-- ═══════════════════════════ PROJECTS ═══════════════════════════ -->
## 🛠️ Personal Projects

<table>
<tr>
<td width="50%" valign="top">

### 🚀 [VentureVerse](https://github.com/pasindufernando1/VentureVerse)
<sub>Full-stack web platform</sub>

A platform connecting entrepreneurs and investors, with secure auth, Stripe payments, real-time messaging over WebSockets, video meetings, scheduling and PDF reports.

<img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=white" alt="React" /> <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white" alt="Stripe" /> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT" />

</td>
<td width="50%" valign="top">

### 📡 [Sri-Tel](https://github.com/pasindufernando1/Sri-Tel)
<sub>Microservices architecture</sub>

A customer-care platform prototype for a telecom company, built as Spring Cloud microservices: service discovery, a config server, an API gateway and services for billing, payments, roaming, notifications and live chat.

<img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java" /> <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white" alt="Spring Cloud" /> <img src="https://img.shields.io/badge/Eureka-6DB33F?style=flat-square" alt="Eureka" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=white" alt="React" /> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🩸 [LIFELINE](https://github.com/pasindufernando1/LIFELINE-second-year-group-project-CS-Group-38-)
<sub>Full-stack web application</sub>

A blood donation management system linking donors, blood banks, hospitals and organisations, with donation campaigns, donor cards and badges, blood requests, inventory, payments, email alerts and PDF reports.

<img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white" alt="PHP" /> <img src="https://img.shields.io/badge/MVC-555555?style=flat-square" alt="MVC" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript" /> <img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white" alt="Stripe" />

</td>
<td width="50%" valign="top">

### ⚙️ [Multithreaded Web Server in C](https://github.com/pasindufernando1/Multithreaded---Webserver-using-C)
<sub>Systems programming</sub>

An HTTP web server written from scratch in C using POSIX sockets and a pthreads thread pool. It handles concurrent clients and serves static HTML, CSS, JS, images, PDFs and video with the correct MIME types.

<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=white" alt="C" /> <img src="https://img.shields.io/badge/POSIX_Sockets-333333?style=flat-square" alt="POSIX Sockets" /> <img src="https://img.shields.io/badge/pthreads-333333?style=flat-square" alt="pthreads" /> <img src="https://img.shields.io/badge/HTTP-005A9C?style=flat-square" alt="HTTP" /> <img src="https://img.shields.io/badge/Make-427819?style=flat-square" alt="Make" />

</td>
</tr>
</table>

<!-- ═══════════════════════════ SKILLS ═══════════════════════════ -->
## 🧰 Tech Stack

<h4>💻 Languages</h4>
<p>
  <img src="https://skillicons.dev/icons?i=java" height="48" alt="Java" title="Java" />
  <img src="./assets/ballerina.svg" height="48" alt="Ballerina" title="Ballerina" />
  <img src="https://skillicons.dev/icons?i=c" height="48" alt="C" title="C" />
  <img src="https://skillicons.dev/icons?i=go" height="48" alt="Go" title="Go" />
  <img src="https://skillicons.dev/icons?i=ts" height="48" alt="TypeScript" title="TypeScript" />
  <img src="https://skillicons.dev/icons?i=js" height="48" alt="JavaScript" title="JavaScript" />
  <img src="https://skillicons.dev/icons?i=kotlin" height="48" alt="Kotlin" title="Kotlin" />
  <img src="https://skillicons.dev/icons?i=python" height="48" alt="Python" title="Python" />
  <img src="https://skillicons.dev/icons?i=cpp" height="48" alt="C++" title="C++" />
  <img src="https://skillicons.dev/icons?i=php" height="48" alt="PHP" title="PHP" />
  <img src="https://skillicons.dev/icons?i=scala" height="48" alt="Scala" title="Scala" />
  <img src="https://skillicons.dev/icons?i=r" height="48" alt="R" title="R" />
</p>

<h4>⚙️ Backend & Microservices</h4>
<p>
  <img src="https://skillicons.dev/icons?i=spring,nodejs,express,maven,gradle&perline=12" alt="Spring, Node.js, Express, Maven, Gradle" />
  <br/>
  <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=for-the-badge&logo=spring&logoColor=white" alt="Spring Cloud" />
  <img src="https://img.shields.io/badge/Gin-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Gin" />
  <img src="https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="Socket.io" />
  <img src="https://img.shields.io/badge/OpenAPI-6BA539?style=for-the-badge&logo=openapiinitiative&logoColor=white" alt="OpenAPI" />
</p>

<h4>🧰 Developer Tooling</h4>
<p>
  <img src="https://img.shields.io/badge/Language_Server_Protocol-20B6B0?style=for-the-badge" alt="Language Server Protocol" />
  <img src="https://img.shields.io/badge/VS_Code_Extensions-007ACC?style=for-the-badge" alt="VS Code Extensions" />
</p>

<h4>🎨 Frontend</h4>
<p>
  <img src="https://skillicons.dev/icons?i=react,html,css,tailwind,materialui,bootstrap,jquery,threejs&perline=12" alt="Frontend" />
</p>

<h4>📱 Mobile</h4>
<p>
  <img src="https://skillicons.dev/icons?i=kotlin,androidstudio&perline=12" alt="Kotlin, Android Studio" />
  <br/>
  <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=for-the-badge&logo=jetpackcompose&logoColor=white" alt="Jetpack Compose" />
</p>

<h4>🗄️ Databases</h4>
<p>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb&perline=12" alt="PostgreSQL, MySQL, MongoDB" />
  <br/>
  <img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="Oracle" />
</p>

<h4>🖥️ Virtualization & Systems</h4>
<p>
  <img src="https://img.shields.io/badge/KVM-CC0000?style=for-the-badge&logo=linux&logoColor=white" alt="KVM" />
  <img src="https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white" alt="QEMU" />
</p>

<h4>☁️ Cloud, DevOps & Tools</h4>
<p>
  <img src="https://skillicons.dev/icons?i=docker,git,github,vscode,linux&perline=12" alt="DevOps & Tools" />
  <br/>
  <img src="https://img.shields.io/badge/Choreo-FF7300?style=for-the-badge&logoColor=white" alt="Choreo" />
  <img src="https://img.shields.io/badge/Asgardeo-FF7300?style=for-the-badge&logoColor=white" alt="Asgardeo" />
</p>

<h4>🖌️ Design</h4>
<p>
  <img src="https://skillicons.dev/icons?i=figma,ps&perline=12" alt="Figma, Photoshop" />
  <br/>
  <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white" alt="Canva" />
</p>

<!-- ═══════════════════════════ FOOTER ═══════════════════════════ -->
<p align="center">
  <i>“First, solve the problem. Then, write the code.”</i>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" width="100%" alt="footer" />
</p>
