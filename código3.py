import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Quiz Portugol", page_icon="💻", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Syne:wght@400;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Syne', sans-serif; }
.stApp { background: #0d1117; color: #e6edf3; }
.quiz-title {
    font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800;
    background: linear-gradient(135deg, #58a6ff, #3fb950);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}
.quiz-subtitle { color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem; }
.step-indicator { display: flex; gap: 8px; margin-bottom: 1rem; }
.step-dot { width: 10px; height: 10px; border-radius: 50%; background: #30363d; display:inline-block; }
.step-dot.active { background: #58a6ff; }
.step-dot.done   { background: #3fb950; }
.score-box {
    background: linear-gradient(135deg, #161b22, #1c2128);
    border: 1px solid #30363d; border-radius: 16px;
    padding: 2rem; text-align: center; margin-top: 1rem;
}
.score-number {
    font-size: 4rem; font-weight: 800;
    background: linear-gradient(135deg, #58a6ff, #3fb950);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
hr { border-color: #21262d !important; }
.stButton > button {
    background-color: #58a6ff !important;  /* azul claro */
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}
.stButton > button:hover {
    background-color: #191970 !important; /* azul mais claro no hover */
}

/* Código */
.code-block {
    background: #161b22; border: 1px solid #30363d; border-radius: 12px;
    padding: 1.1rem 1.4rem; font-family: 'Fira Code', monospace;
    font-size: .88rem; line-height: 2rem; color: #c9d1d9;
    margin-bottom: 1rem; overflow-x: auto;
}
.code-row { display: flex; align-items: center; flex-wrap: wrap; gap: 4px; min-height: 2rem; }
.ct { white-space: pre; }
.gap-correct {
    display: inline-block; padding: 2px 10px; border-radius: 6px;
    border: 2px solid #3fb950; color: #3fb950; background: #122318;
    font-weight: 600; font-size: .82rem;
}
.gap-wrong {
    display: inline-block; padding: 2px 10px; border-radius: 6px;
    border: 2px solid #f85149; color: #f85149; background: #2d1313;
    font-weight: 600; font-size: .82rem;
}
.gap-wrong-hint { font-size: .65rem; color: #8b949e; display: block; line-height: 1; }
/* Selectbox compacto */
div[data-testid="stSelectbox"] > div > div {
    background: #21262d !important;
    border: 2px dashed #58a6ff !important;
    border-radius: 6px !important;
    font-family: 'Fira Code', monospace !important;
    font-size: .82rem !important;
    color: #58a6ff !important;
    min-height: 32px !important;
}
div[data-testid="stSelectbox"] label { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ─── EXERCÍCIOS ───────────────────────────────────────────────────────────────

EXERCISES = [
    {
        "titulo": "Estrutura de Repetição — enquanto",
        "linhas": [
            [["t", 'algoritmo "Repeticao"']],
            [["t", "var"]],
            [["t", "   tem_combustivel : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   tem_combustivel <- "], ["g", 2]],
            [["t", "   "], ["g", 3], ["t", " tem_combustivel faca"]],
            [["t", '      escreval("Carro andando...")']],
            [["t", "      tem_combustivel <- "], ["g", 4]],
            [["t", "   "], ["g", 5]],
            [["g", 6]],
        ],
        "gabarito": {"1": "logico", "2": "verdadeiro", "3": "enquanto", "4": "falso", "5": "fimenquanto", "6": "fimalgoritmo"},
        "opcoes": ["logico", "verdadeiro", "enquanto", "falso", "fimenquanto", "fimalgoritmo", "inteiro", "real", "fimse"],
    },
    {
        "titulo": "Estrutura Condicional — se...entao...senao",
        "linhas": [
            [["t", 'algoritmo "Condicional"']],
            [["t", "var"]],
            [["t", "   nota : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   "], ["g", 2], ["t", '("Digite sua nota:")']],
            [["t", "   "], ["g", 3], ["t", "(nota)"]],
            [["t", "   "], ["g", 4], ["t", " nota >= 7 entao"]],
            [["t", '      escreval("Aprovado!")']],
            [["t", "   "], ["g", 5]],
            [["t", '      escreval("Reprovado!")']],
            [["t", "   "], ["g", 6]],
            [["t", "fimalgoritmo"]],
        ],
        "gabarito": {"1": "inteiro", "2": "escreva", "3": "leia", "4": "se", "5": "senao", "6": "fimse"},
        "opcoes": ["inteiro", "escreva", "leia", "se", "senao", "fimse", "logico", "enquanto", "fimalgoritmo"],
    },
    {
        "titulo": "Estrutura de Escolha — escolha...seja",
        "linhas": [
            [["t", 'algoritmo "EscolhaDia"']],
            [["t", "var"]],
            [["t", "   dia : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   "], ["g", 2], ["t", '("Digite o dia (1-3):")']],
            [["t", "   "], ["g", 3], ["t", "(dia)"]],
            [["t", "   "], ["g", 4], ["t", " dia "], ["g", 5]],
            [["t", '      1: escreval("Segunda-feira")']],
            [["t", '      2: escreval("Terca-feira")']],
            [["t", '      3: escreval("Quarta-feira")']],
            [["t", '      outrocaso: escreval("Dia invalido")']],
            [["t", "   "], ["g", 6]],
            [["t", "fimalgoritmo"]],
        ],
        "gabarito": {"1": "inteiro", "2": "escreva", "3": "leia", "4": "escolha", "5": "seja", "6": "fimescolha"},
        "opcoes": ["inteiro", "escreva", "leia", "escolha", "seja", "fimescolha", "logico", "se", "fimse"],
    },
]


# ─── SESSION STATE ────────────────────────────────────────────────────────────

def init():
    defaults = {
        "fase": "nome",          # "nome" | "quiz" | "resultado_ex" | "final"
        "nome_aluno": "",
        "ex_idx": 0,
        "respostas_ex": [{} for _ in EXERCISES],    # respostas brutas por exercício
        "resultados_ex": [None for _ in EXERCISES], # dict gap->bool por exercício
        "acertos_ex": [0] * len(EXERCISES),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

# ─── HEADER ──────────────────────────────────────────────────────────────────

st.markdown('<div class="quiz-title">💻 Quiz Portugol</div>', unsafe_allow_html=True)

if st.session_state.fase not in ("nome", "final"):
    st.markdown('<div class="quiz-subtitle">Preencha as lacunas com os termos corretos.</div>', unsafe_allow_html=True)
    dots = '<div class="step-indicator">'
    for i in range(len(EXERCISES)):
        cls = "done" if i < st.session_state.ex_idx else ("active" if i == st.session_state.ex_idx else "")
        dots += f'<div class="step-dot {cls}"></div>'
    dots += '</div>'
    st.markdown(dots, unsafe_allow_html=True)

# ─── FASE: NOME ──────────────────────────────────────────────────────────────

if st.session_state.fase == "nome":
    st.markdown('<div class="quiz-subtitle">Bem-vindo! Informe seu nome para começar.</div>', unsafe_allow_html=True)
    st.markdown("---")
    nome = st.text_input("👤 Seu nome", placeholder="Digite seu nome completo...")
    if st.button("▶ Iniciar Quiz", use_container_width=True, disabled=not nome.strip()):
        st.session_state.nome_aluno = nome.strip()
        st.session_state.fase = "quiz"
        st.rerun()
    st.stop()

# ─── FASE: RESULTADO FINAL ────────────────────────────────────────────────────

if st.session_state.fase == "final":
    total_lac = sum(len(ex["gabarito"]) for ex in EXERCISES)
    total_ac  = sum(st.session_state.acertos_ex)
    emoji = "🏆" if total_ac == total_lac else ("👍" if total_ac >= total_lac // 2 else "📚")
    msg   = ("Perfeito! Você domina Portugol!" if total_ac == total_lac else
             "Muito bem! Continue praticando!" if total_ac >= total_lac // 2 else
             "Continue estudando, você vai melhorar!")
    st.markdown(f"""
    <div class="score-box">
        <div style="font-size:3rem">{emoji}</div>
        <div style="font-size:1.1rem;color:#8b949e;margin-bottom:.3rem">
            {st.session_state.nome_aluno}
        </div>
        <div class="score-number">{total_ac}/{total_lac}</div>
        <div style="color:#8b949e;margin-top:.5rem;font-size:1rem">{msg}</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    for i, ex in enumerate(EXERCISES):
        ac  = st.session_state.acertos_ex[i]
        tot = len(ex["gabarito"])
        cor = "#3fb950" if ac == tot else ("#f0883e" if ac >= tot // 2 else "#f85149")
        st.markdown(f"- **Ex {i+1}** — {ex['titulo']}: <span style='color:{cor}'>{ac}/{tot}</span>", unsafe_allow_html=True)


    if st.button("🔄 Recomeçar", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
    st.stop()

# ─── FASE: QUIZ ───────────────────────────────────────────────────────────────

idx      = st.session_state.ex_idx
ex       = EXERCISES[idx]
gabarito = ex["gabarito"]
opcoes   = ex["opcoes"]
verificado = st.session_state.resultados_ex[idx] is not None

st.markdown(f"### Exercício {idx+1}/{len(EXERCISES)} — {ex['titulo']}")
st.markdown(f"<div style='color:#8b949e;font-size:.85rem;margin-bottom:.5rem'>👤 {st.session_state.nome_aluno}</div>", unsafe_allow_html=True)

# ─── Renderiza código com lacunas ─────────────────────────────────────────────

# Coleta as lacunas em ordem para renderizar os selectboxes inline
gap_ids_em_ordem = []
for linha in ex["linhas"]:
    for tipo, val in linha:
        if tipo == "g":
            gap_ids_em_ordem.append(str(val))

# Renderiza o bloco de código com HTML + selectboxes do Streamlit intercalados
# Como Streamlit não permite HTML+widgets misturados, usamos colunas por linha

st.markdown('<div class="code-block">', unsafe_allow_html=True)

for linha in ex["linhas"]:
    # Conta quantas lacunas há nessa linha
    gaps_na_linha = [str(val) for tipo, val in linha if tipo == "g"]
    n_gaps = len(gaps_na_linha)

    if n_gaps == 0:
        # Linha só texto
        texto = "".join(val for tipo, val in linha if tipo == "t")
        if verificado:
            st.markdown(f'<div class="code-row"><span class="ct">{texto}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="code-row"><span class="ct">{texto}</span></div>', unsafe_allow_html=True)
    else:
        # Linha com lacunas — monta colunas
        # Primeiro conta quantos segmentos temos (textos + gaps alternados)
        partes = linha  # lista de [tipo, val]

        if verificado:
            # Pós-resultado: mostra tudo em HTML com classes correct/wrong
            html_row = '<div class="code-row">'
            for tipo, val in partes:
                if tipo == "t":
                    html_row += f'<span class="ct">{val}</span>'
                else:
                    gid = str(val)
                    resp = st.session_state.respostas_ex[idx].get(gid, "??")
                    ok   = st.session_state.resultados_ex[idx].get(gid, False)
                    certo = gabarito[gid]
                    cls  = "gap-correct" if ok else "gap-wrong"
                    hint = "" if ok else f'<span class="gap-wrong-hint">✓ {certo}</span>'
                    html_row += f'<span class="{cls}">{resp}{hint}</span>'
            html_row += '</div>'
            st.markdown(html_row, unsafe_allow_html=True)
        else:
            # Pré-resultado: textos em HTML, lacunas como selectbox
            # Usa colunas — proporção: textos finos, gaps largos
            col_defs = []
            for tipo, val in partes:
                if tipo == "t":
                    col_defs.append(max(len(val) * 0.12, 1))
                else:
                    col_defs.append(2)

            cols = st.columns(col_defs)
            col_i = 0
            for tipo, val in partes:
                with cols[col_i]:
                    if tipo == "t":
                        st.markdown(f'<span class="ct" style="font-family:\'Fira Code\',monospace;font-size:.88rem;color:#c9d1d9;white-space:pre">{val}</span>', unsafe_allow_html=True)
                    else:
                        gid = str(val)
                        key = f"gap_{idx}_{gid}"
                        opcoes_gap = ["— escolha —"] + opcoes
                        atual = st.session_state.respostas_ex[idx].get(gid)
                        idx_atual = (opcoes_gap.index(atual) if atual and atual in opcoes_gap else 0)
                        escolha = st.selectbox(
                            label=f"gap{gid}",
                            options=opcoes_gap,
                            index=idx_atual,
                            key=key,
                            label_visibility="collapsed"
                        )
                        if escolha != "— escolha —":
                            st.session_state.respostas_ex[idx][gid] = escolha
                        elif gid in st.session_state.respostas_ex[idx]:
                            del st.session_state.respostas_ex[idx][gid]
                col_i += 1

st.markdown('</div>', unsafe_allow_html=True)

# ─── FASE: RESULTADO DO EXERCÍCIO ─────────────────────────────────────────────

if st.session_state.fase == "resultado_ex":
    resultados = st.session_state.resultados_ex[idx]
    acertos    = st.session_state.acertos_ex[idx]
    total      = len(gabarito)
    cor = "#3fb950" if acertos == total else ("#f0883e" if acertos >= total // 2 else "#f85149")
    st.markdown(f"""
    <div style="text-align:center;padding:10px;border-radius:8px;
         color:{cor};background:{cor}18;border:1px solid {cor}44;
         font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;margin-bottom:.8rem">
        🎯 {acertos}/{total} acertos neste exercício
    </div>""", unsafe_allow_html=True)

    is_last = idx == len(EXERCISES) - 1
    label   = "Ver Resultado Final 🏁" if is_last else "Próximo Exercício →"
    if st.button(label, use_container_width=True):
        if is_last:
            st.session_state.fase = "final"
        else:
            st.session_state.ex_idx += 1
            st.session_state.fase = "quiz"
        st.rerun()
    st.stop()

# ─── BOTÕES DE AÇÃO ──────────────────────────────────────────────────────────

st.markdown("---")
col1, col2 = st.columns([3, 1])

respostas_atuais = st.session_state.respostas_ex[idx]
todas_preenchidas = all(str(k) in respostas_atuais for k in gabarito)

with col1:
    if st.button("✅ Verificar Respostas", use_container_width=True, disabled=not todas_preenchidas):
        # Calcula resultado
        res = {k: (respostas_atuais.get(k) == v) for k, v in gabarito.items()}
        acertos = sum(1 for v in res.values() if v)
        st.session_state.resultados_ex[idx] = res
        st.session_state.acertos_ex[idx]    = acertos
        st.session_state.fase = "resultado_ex"
        st.rerun()

with col2:
    if st.button("🗑 Limpar", use_container_width=True):
        st.session_state.respostas_ex[idx] = {}
        st.rerun()

if not todas_preenchidas:
    faltam = len(gabarito) - len(respostas_atuais)
    st.markdown(f"<div style='color:#8b949e;font-size:.78rem;margin-top:.3rem'>⚠️ Preencha ainda {faltam} lacuna(s) para verificar.</div>", unsafe_allow_html=True)
