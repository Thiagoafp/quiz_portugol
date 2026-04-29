import streamlit as st

st.set_page_config(page_title="Quiz Lógica", page_icon="💻", layout="centered")

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
.quiz-card {
    background: #161b22; border: 1px solid #30363d; border-radius: 16px;
    padding: 1.5rem; text-align: center; cursor: pointer;
    transition: border-color 0.2s;
}
.quiz-card:hover { border-color: #58a6ff; }
.quiz-card-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.quiz-card-title { font-size: 1.1rem; font-weight: 700; color: #e6edf3; }
.quiz-card-desc  { font-size: 0.8rem; color: #8b949e; margin-top: 0.3rem; }
hr { border-color: #21262d !important; }
.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
}
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

# ─── BANCO DE EXERCÍCIOS ──────────────────────────────────────────────────────

QUIZZES = {
    "portugol": {
        "titulo": "Quiz Portugol",
        "icone": "💻",
        "desc": "Estruturas de controle e repetição",
        "exercises": [
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
                    [["t", "   "], ["g", 2], ["t", '("Digite o dia (1-3):')],
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
        ],
    },

    "matematica": {
        "titulo": "Quiz Matemática",
        "icone": "🧮",
        "desc": "Operações matemáticas em lógica de programação",
        "exercises": [
            {
                "titulo": "Operações Básicas — soma e subtração",
                "linhas": [
                    [["t", 'algoritmo "OperacoesBasicas"']],
                    [["t", "var"]],
                    [["t", "   a, b, resultado : "], ["g", 1]],
                    [["t", "inicio"]],
                    [["t", "   "], ["g", 2], ["t", '("Digite o primeiro numero: ")']],
                    [["t", "   leia(a)"]],
                    [["t", "   escreva("], ["g", 3], ["t", ')']],
                    [["t", "   leia(b)"]],
                    [["t", "   resultado <- "], ["g", 4], ["t", " + b"]],
                    [["t", "   escreva("], ["g", 5], ["t", ')']],
                    [["t", "   resultado <- a "], ["g", 6], ["t", " b"]],
                    [["t", '   escreval("Subtracao: ", resultado)']],
                    [["t", "fimalgoritmo"]],
                ],
                "gabarito": {
                    "1": "inteiro",
                    "2": "escreva",
                    "3": '"Digite o segundo numero: "',
                    "4": "a",
                    "5": '"Soma: ", resultado',
                    "6": "-",
                },
                "opcoes": [
                    "inteiro",
                    "escreva",
                    '"Digite o segundo numero: "',
                    "a",
                    '"Soma: ", resultado',
                    "-",
                    "real",
                    "+",
                    "leia",
                ],
            },
            {
                "titulo": "Multiplicação e Divisão",
                "linhas": [
                    [["t", 'algoritmo "MultiDiv"']],
                    [["t", "var"]],
                    [["t", "   a, b : "], ["g", 1]],
                    [["t", "   resultado : "], ["g", 2]],
                    [["t", "inicio"]],
                    [["t", "   leia(a)"]],
                    [["t", "   leia(b)"]],
                    [["t", "   resultado <- a "], ["g", 3], ["t", " b"]],
                    [["t", '   escreval("Multiplicacao: ", resultado)']],
                    [["t", "   "], ["g", 4], ["t", " b "], ["g", 5], ["t", " 0 entao"]],
                    [["t", "      resultado <- a "], ["g", 6], ["t", " b"]],
                    [["t", '      escreval("Divisao: ", resultado)']],
                    [["t", "   fimse"]],
                    [["t", "fimalgoritmo"]],
                ],
                "gabarito": {
                    "1": "inteiro",
                    "2": "real",
                    "3": "*",
                    "4": "se",
                    "5": "<>",
                    "6": "/",
                },
                "opcoes": ["inteiro", "real", "*", "se", "<>", "/", "logico", "+", "="],
            },
            {
                "titulo": "Média e Comparação",
                "linhas": [
                    [["t", 'algoritmo "Media"']],
                    [["t", "var"]],
                    [["t", "   n1, n2, n3, media : "], ["g", 1]],
                    [["t", "inicio"]],
                    [["t", "   leia(n1)"]],
                    [["t", "   leia(n2)"]],
                    [["t", "   leia(n3)"]],
                    [["t", "   media <- (n1 "], ["g", 2], ["t", " n2 + n3) "], ["g", 3], ["t", " 3"]],
                    [["t", '   escreval("Media: ", media)']],
                    [["t", "   "], ["g", 4], ["t", " media >= 7 entao"]],
                    [["t", '      escreval("Aprovado!")']],
                    [["t", "   "], ["g", 5]],
                    [["t", '      escreval("Reprovado!")']],
                    [["t", "   "], ["g", 6]],
                    [["t", "fimalgoritmo"]],
                ],
                "gabarito": {
                    "1": "real",
                    "2": "+",
                    "3": "/",
                    "4": "se",
                    "5": "senao",
                    "6": "fimse",
                },
                "opcoes": ["real", "+", "/", "se", "senao", "fimse", "inteiro", "*", "-"],
            },
        ],
    },
}

# ─── SESSION STATE ────────────────────────────────────────────────────────────

def init():
    defaults = {
        "fase": "selecao",       # "selecao" | "quiz" | "resultado_ex" | "final"
        "quiz_ativo": None,
        "ex_idx": 0,
        "respostas_ex": None,
        "resultados_ex": None,
        "acertos_ex": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

def iniciar_quiz(quiz_key):
    exercises = QUIZZES[quiz_key]["exercises"]
    st.session_state.quiz_ativo   = quiz_key
    st.session_state.fase         = "quiz"
    st.session_state.ex_idx       = 0
    st.session_state.respostas_ex = [{} for _ in exercises]
    st.session_state.resultados_ex= [None for _ in exercises]
    st.session_state.acertos_ex   = [0] * len(exercises)

# ─── HEADER ──────────────────────────────────────────────────────────────────

quiz_atual = QUIZZES.get(st.session_state.quiz_ativo, {})
titulo = quiz_atual.get("titulo", "Quiz Lógica de Programação")
st.markdown(f'<div class="quiz-title">{quiz_atual.get("icone","💻")} {titulo}</div>', unsafe_allow_html=True)

# ─── FASE: SELEÇÃO ────────────────────────────────────────────────────────────

if st.session_state.fase == "selecao":
    st.markdown('<div class="quiz-subtitle">Escolha o quiz que deseja fazer:</div>', unsafe_allow_html=True)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="quiz-card">
            <div class="quiz-card-icon">💻</div>
            <div class="quiz-card-title">Quiz Portugol</div>
            <div class="quiz-card-desc">Estruturas de controle e repetição em Portugol</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("▶ Iniciar", key="btn_portugol", use_container_width=True):
            iniciar_quiz("portugol")
            st.rerun()
    with col2:
        st.markdown("""
        <div class="quiz-card">
            <div class="quiz-card-icon">🧮</div>
            <div class="quiz-card-title">Quiz Matemática</div>
            <div class="quiz-card-desc">Operações matemáticas em lógica de programação</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("▶ Iniciar", key="btn_matematica", use_container_width=True):
            iniciar_quiz("matematica")
            st.rerun()
    st.stop()

# ─── FASE: RESULTADO FINAL ────────────────────────────────────────────────────

exercises = QUIZZES[st.session_state.quiz_ativo]["exercises"]

if st.session_state.fase == "final":
    total_lac = sum(len(ex["gabarito"]) for ex in exercises)
    total_ac  = sum(st.session_state.acertos_ex)
    emoji = "🏆" if total_ac == total_lac else ("👍" if total_ac >= total_lac // 2 else "📚")
    msg   = ("Perfeito! Mandou bem!" if total_ac == total_lac else
             "Muito bem! Continue praticando!" if total_ac >= total_lac // 2 else
             "Continue estudando, você vai melhorar!")
    st.markdown(f"""
    <div class="score-box">
        <div style="font-size:3rem">{emoji}</div>
        <div class="score-number">{total_ac}/{total_lac}</div>
        <div style="color:#8b949e;margin-top:.5rem;font-size:1rem">{msg}</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    for i, ex in enumerate(exercises):
        ac  = st.session_state.acertos_ex[i]
        tot = len(ex["gabarito"])
        cor = "#3fb950" if ac == tot else ("#f0883e" if ac >= tot // 2 else "#f85149")
        st.markdown(f"- **Ex {i+1}** — {ex['titulo']}: <span style='color:{cor}'>{ac}/{tot}</span>", unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Refazer este quiz", use_container_width=True):
            iniciar_quiz(st.session_state.quiz_ativo)
            st.rerun()
    with col2:
        if st.button("🏠 Escolher outro quiz", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
    st.stop()

# ─── FASE: QUIZ ───────────────────────────────────────────────────────────────

idx        = st.session_state.ex_idx
ex         = exercises[idx]
gabarito   = ex["gabarito"]
opcoes     = ex["opcoes"]
verificado = st.session_state.resultados_ex[idx] is not None

# Indicador de progresso
dots = '<div class="step-indicator">'
for i in range(len(exercises)):
    cls = "done" if i < idx else ("active" if i == idx else "")
    dots += f'<div class="step-dot {cls}"></div>'
dots += '</div>'
st.markdown(dots, unsafe_allow_html=True)

st.markdown(f"### Exercício {idx+1}/{len(exercises)} — {ex['titulo']}")
st.markdown('<div class="quiz-subtitle">Preencha as lacunas com os termos corretos.</div>', unsafe_allow_html=True)

# ─── Renderiza código ─────────────────────────────────────────────────────────

st.markdown('<div class="code-block">', unsafe_allow_html=True)

for linha in ex["linhas"]:
    gaps_na_linha = [str(val) for tipo, val in linha if tipo == "g"]

    if not gaps_na_linha:
        texto = "".join(val for tipo, val in linha if tipo == "t")
        st.markdown(f'<div class="code-row"><span class="ct">{texto}</span></div>', unsafe_allow_html=True)
    else:
        partes = linha
        if verificado:
            html_row = '<div class="code-row">'
            for tipo, val in partes:
                if tipo == "t":
                    html_row += f'<span class="ct">{val}</span>'
                else:
                    gid   = str(val)
                    resp  = st.session_state.respostas_ex[idx].get(gid, "??")
                    ok    = st.session_state.resultados_ex[idx].get(gid, False)
                    certo = gabarito[gid]
                    cls   = "gap-correct" if ok else "gap-wrong"
                    hint  = "" if ok else f'<span class="gap-wrong-hint">✓ {certo}</span>'
                    html_row += f'<span class="{cls}">{resp}{hint}</span>'
            html_row += '</div>'
            st.markdown(html_row, unsafe_allow_html=True)
        else:
            col_defs = []
            for tipo, val in partes:
                col_defs.append(max(len(str(val)) * 0.12, 1) if tipo == "t" else 2)

            cols = st.columns(col_defs)
            for col_i, (tipo, val) in enumerate(partes):
                with cols[col_i]:
                    if tipo == "t":
                        st.markdown(f'<span class="ct" style="font-family:\'Fira Code\',monospace;font-size:.88rem;color:#c9d1d9;white-space:pre">{val}</span>', unsafe_allow_html=True)
                    else:
                        gid  = str(val)
                        key  = f"gap_{st.session_state.quiz_ativo}_{idx}_{gid}"
                        opts = ["— escolha —"] + opcoes
                        atual   = st.session_state.respostas_ex[idx].get(gid)
                        idx_sel = (opts.index(atual) if atual and atual in opts else 0)
                        escolha = st.selectbox(
                            label=f"gap{gid}", options=opts,
                            index=idx_sel, key=key,
                            label_visibility="collapsed"
                        )
                        if escolha != "— escolha —":
                            st.session_state.respostas_ex[idx][gid] = escolha
                        elif gid in st.session_state.respostas_ex[idx]:
                            del st.session_state.respostas_ex[idx][gid]

st.markdown('</div>', unsafe_allow_html=True)

# ─── RESULTADO DO EXERCÍCIO ───────────────────────────────────────────────────

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

    is_last = idx == len(exercises) - 1
    label   = "Ver Resultado Final 🏁" if is_last else "Próximo Exercício →"
    if st.button(label, use_container_width=True):
        if is_last:
            st.session_state.fase = "final"
        else:
            st.session_state.ex_idx += 1
            st.session_state.fase = "quiz"
        st.rerun()
    st.stop()

# ─── BOTÕES DE AÇÃO ───────────────────────────────────────────────────────────

st.markdown("---")
col1, col2 = st.columns([3, 1])

respostas_atuais  = st.session_state.respostas_ex[idx]
todas_preenchidas = all(str(k) in respostas_atuais for k in gabarito)

with col1:
    if st.button("✅ Verificar Respostas", use_container_width=True, disabled=not todas_preenchidas):
        res     = {k: (respostas_atuais.get(k) == v) for k, v in gabarito.items()}
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
