from flask import Flask, render_template_string
import os

app = Flask(__name__, static_folder='static')

HTML_TEMPLATE = '''
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Oficina RBG - Mecânica e Auto Elétrica</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      html, body {
        height: 100%;
      }
      body {
        font-family: 'Montserrat', system-ui, -apple-system, 'Segoe UI', Roboto;
        background: #000;
        color: #fff;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
      }
      header {
        background: #000;
        border-bottom: 3px solid #dc143c;
        padding: 1rem 2rem;
        position: sticky;
        top: 0;
        z-index: 100;
        display: flex;
        justify-content: flex-end;
      }
      nav a {
        color: #fff;
        text-decoration: none;
        margin: 0 1.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: color 0.3s;
      }
      nav a:hover {
        color: #dc143c;
      }
      nav a.active {
        color: #dc143c;
        border-bottom: 2px solid #dc143c;
        padding-bottom: 0.5rem;
      }
      .page {
        display: none;
        min-height: calc(100vh - 70px);
      }
      .page.active {
        display: block;
      }
      .hero {
        background: #1a1a1a;
        padding: 6rem 2rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
      }
      .logo-hero {
        max-width: 400px;
        margin: 0 auto 2rem;
        animation: slideDown 0.6s ease-out;
        filter: drop-shadow(0 0 30px rgba(220, 20, 60, 0.2));
      }
      @keyframes slideDown {
        from {
          opacity: 0;
          transform: translateY(-20px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
      .hero h1 {
        font-size: 3.5rem;
        color: #dc143c;
        margin-bottom: 0.5rem;
        font-weight: 900;
      }
      .hero p {
        font-size: 1.3rem;
        color: #fff;
        margin-bottom: 2rem;
      }
      .cta-btn {
        background: #dc143c;
        color: #fff;
        padding: 1rem 2rem;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 700;
        display: inline-block;
        transition: background 0.3s;
        cursor: pointer;
        border: none;
      }
      .cta-btn:hover {
        background: #b01030;
      }
      section {
        padding: 3rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
        animation: fadeIn 0.5s ease-in;
      }
      @keyframes fadeIn {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }
      h2 {
        font-size: 2.5rem;
        color: #dc143c;
        margin-bottom: 2rem;
        text-align: center;
        border-bottom: 2px solid #dc143c;
        padding-bottom: 1rem;
      }
      .services {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        max-width: 1000px;
        margin: 0 auto;
      }
      .service-card {
        background: #1a1a1a;
        padding: 2rem;
        border-left: 4px solid #dc143c;
        border-radius: 5px;
        transition: transform 0.3s;
      }
      .service-card:hover {
        transform: translateY(-5px);
        background: #2a2a2a;
      }
      .service-card h3 {
        color: #dc143c;
        margin-bottom: 1rem;
        font-size: 1.3rem;
      }
      .service-card p {
        color: #ccc;
        line-height: 1.6;
      }
      .about {
        background: #1a1a1a;
        padding: 2rem;
        border-radius: 5px;
        border-left: 4px solid #dc143c;
      }
      .about h3 {
        color: #dc143c;
        margin-bottom: 1rem;
      }
      .about p {
        color: #ccc;
        line-height: 1.8;
        margin-bottom: 1rem;
      }
      .contact-info {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
      }
      .contact-item {
        background: #1a1a1a;
        padding: 1.5rem;
        border-radius: 5px;
        text-align: center;
        border-top: 3px solid #dc143c;
      }
      .contact-item h4 {
        color: #dc143c;
        margin-bottom: 0.5rem;
      }
      .contact-item p {
        color: #ccc;
      }
      footer {
        background: #000;
        border-top: 3px solid #dc143c;
        padding: 2rem;
        text-align: center;
        color: #999;
      }
      @media (max-width: 768px) {
        nav a {
          margin: 0 1rem;
          font-size: 0.9rem;
        }
        .hero h1 {
          font-size: 2.5rem;
        }
        h2 {
          font-size: 1.8rem;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <nav>
        <a onclick="showPage(\'home\')" class="nav-link active" data-page="home">Home</a>
        <a onclick="showPage(\'servicos\')" class="nav-link" data-page="servicos">Serviços</a>
        <a onclick="showPage(\'sobre\')" class="nav-link" data-page="sobre">Sobre</a>
        <a onclick="showPage(\'contato\')" class="nav-link" data-page="contato">Contato</a>
      </nav>
    </header>

    <!-- HOME PAGE -->
    <div id="home" class="page active">
      <section class="hero">
        <img src="{{ url_for(\'static\', filename=\'images/logo.png\') }}" alt="Logo RBG" class="logo-hero">
        <button class="cta-btn" onclick="showPage(\'contato\')">Solicitar Orçamento</button>
      </section>
    </div>

    <!-- SERVIÇOS PAGE -->
    <div id="servicos" class="page">
      <section>
        <h2>Nossos Serviços</h2>
        <div class="services">
          <div class="service-card">
            <h3>⚙️ Mecânica Geral</h3>
            <p>Manutenção preventiva e corretiva, revisões completas, troca de óleo, filtros, correntes e correias.</p>
          </div>
          <div class="service-card">
            <h3>⚡ Auto Elétrica</h3>
            <p>Diagnóstico elétrico, bateria, alternador, motor de arranque, sistema de iluminação e injeção eletrônica.</p>
          </div>
          <div class="service-card">
            <h3>🔧 Suspensão e Freios</h3>
            <p>Alinhamento, balanceamento, amortecedores, discos, pastilhas e cilindros de freio.</p>
          </div>
          <div class="service-card">
            <h3> Diagnóstico Computadorizado</h3>
            <p>Leitura de códigos de falha, diagnóstico avançado de sistemas eletrônicos modernos.</p>
          </div>
        </div>
      </section>
      <footer>
        <p>&copy; 2025 Oficina RBG. Todos os direitos reservados.</p>
      </footer>
    </div>

    <!-- SOBRE PAGE -->
    <div id="sobre" class="page">
      <section>
        <h2>Sobre a Oficina RBG</h2>
        <div class="about">
          <h3>Qualidade e Confiança desde 2015</h3>
          <p>A Oficina RBG é referência em serviços de mecânica e auto elétrica na região, com mais de 8 anos de experiência atendendo clientes satisfeitos.</p>
          <p>Contamos com profissionais qualificados, equipamentos modernos e peças originais, garantindo o melhor atendimento para seu veículo.</p>
          <h3 style="margin-top: 1.5rem;">Por que escolher a RBG?</h3>
          <ul style="margin-left: 1.5rem; color: #ccc; line-height: 2;">
            <li>✓ Equipe de técnicos certificados</li>
            <li>✓ Equipamentos de ponta</li>
            <li>✓ Garantia em serviços</li>
            <li>✓ Preços competitivos</li>
            <li>✓ Atendimento personalizado</li>
          </ul>
        </div>
      </section>
      <footer>
        <p>&copy; 2025 Oficina RBG. Todos os direitos reservados.</p>
      </footer>
    </div>

    <!-- CONTATO PAGE -->
    <div id="contato" class="page">
      <section>
        <h2>Contato</h2>
        <div class="contact-info">
          <div class="contact-item">
            <h4>📍 Endereço</h4>
            <p>Rua Joaquim Marciano 6-72<br>Jardim TV<br>Bauru - SP</p>
          </div>
          <div class="contact-item">
            <h4>📞 Telefone</h4>
            <p>(14) 98803-0831<br>WhatsApp disponível</p>
          </div>
          <div class="contact-item">
            <h4>🕐 Horário</h4>
            <p>Seg-Sex: 8h às 18h<br>Sáb: 8h às 14h<br>Dom: Fechado</p>
          </div>
        </div>
      </section>
      <footer>
        <p>&copy; 2025 Oficina RBG. Todos os direitos reservados.</p>
      </footer>
    </div>

    <script>
      function showPage(pageId) {
        // Esconde todas as páginas
        const pages = document.querySelectorAll(\'.page\');
        pages.forEach(page => page.classList.remove(\'active\'));
        
        // Remove active de todos os links de navegação
        const navLinks = document.querySelectorAll(\'.nav-link\');
        navLinks.forEach(link => link.classList.remove(\'active\'));
        
        // Mostra a página selecionada
        document.getElementById(pageId).classList.add(\'active\');
        
        // Marca o link como ativo
        document.querySelector(`[data-page="${pageId}"]`).classList.add(\'active\');
        
        // Scroll para o topo
        window.scrollTo(0, 0);
      }
    </script>
  </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
