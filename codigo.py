import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Atividades Aula", page_icon="💻", layout="centered")

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
    background-color: #58a6ff !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}
.stButton > button:hover {
    background-color: #191970 !important;
}

/* Menu de atividades */
.menu-title {
    font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 800;
    color: #e6edf3; text-align: center; margin-bottom: 1.5rem;
}
.activity-btn {
    display: flex; align-items: center; gap: 12px;
    background: transparent; border: 2px solid #30363d;
    border-radius: 12px; padding: 1rem 1.4rem;
    cursor: pointer; transition: all .2s; margin-bottom: .8rem;
    text-decoration: none; width: 100%;
}
.activity-btn:hover { border-color: #58a6ff; background: #161b22; }
.activity-icon { font-size: 1.4rem; }
.activity-label {
    font-family: 'Syne', sans-serif; font-weight: 700;
    font-size: 1.05rem; color: #e6edf3;
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

# ─── EXERCÍCIOS — QUIZ PORTUGOL ───────────────────────────────────────────────

EXERCISES_PORTUGOL = [
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

# ─── EXERCÍCIOS — OPERAÇÕES BÁSICAS ──────────────────────────────────────────

EXERCISES_OPERACOES = [
    {
        "titulo": "Soma — Ingressos Vendidos",
        "instrucao": "💡 Some dois valores e mostre o resultado. Use o operador + para somar.",
        "linhas": [
            [["t", 'algoritmo "IngressosSoma"']],
            [["t", "var"]],
            [["t", "   // Declaramos duas variáveis inteiras"]],
            [["t", "   dia1, dia2, total : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   // Atribuímos os valores de cada dia"]],
            [["t", "   dia1 <- 30"]],
            [["t", "   dia2 <- 45"]],
            [["t", "   // Somamos os dois dias"]],
            [["t", "   total <- dia1 "], ["g", 2], ["t", " dia2"]],
            [["t", '   escreval("Total de ingressos:")']],
            [["t", "   escreva("], ["g", 3], ["t", ")"]],
            [["g", 4]],
        ],
        "gabarito": {"1": "inteiro", "2": "+", "3": "total", "4": "fimalgoritmo"},
        "opcoes": ["inteiro", "real", "+", "-", "*", "total", "dia1", "fimalgoritmo"],
    },
    {
        "titulo": "Subtração — Vagas Livres",
        "instrucao": "💡 Subtraia para descobrir quantas vagas sobram. Use o operador - para subtrair.",
        "linhas": [
            [["t", 'algoritmo "VagasLivres"']],
            [["t", "var"]],
            [["t", "   // Total de vagas e quantas estão ocupadas"]],
            [["t", "   total, ocupadas, livres : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   total <- 50"]],
            [["t", "   ocupadas <- 18"]],
            [["t", "   // Vagas livres = total menos as ocupadas"]],
            [["t", "   livres <- "], ["g", 2], ["t", " "], ["g", 3], ["t", " ocupadas"]],
            [["t", "   escreva(livres)"]],
            [["g", 4]],
        ],
        "gabarito": {"1": "inteiro", "2": "total", "3": "-", "4": "fimalgoritmo"},
        "opcoes": ["inteiro", "real", "total", "ocupadas", "-", "+", "*", "fimalgoritmo"],
    },
    {
        "titulo": "Multiplicação — Preço Total",
        "instrucao": "💡 Multiplique quantidade pelo preço unitário. Use o operador * para multiplicar.",
        "linhas": [
            [["t", 'algoritmo "PrecoTotal"']],
            [["t", "var"]],
            [["t", "   // Quantidade de itens e preço de cada um"]],
            [["t", "   quantidade, preco, total : "], ["g", 1]],
            [["t", "inicio"]],
            [["t", "   quantidade <- 5"]],
            [["t", "   preco <- 20"]],
            [["t", "   // Total = quantidade vezes o preço"]],
            [["t", "   total <- quantidade "], ["g", 2], ["t", " preco"]],
            [["t", '   escreval("Valor total:")']],
            [["t", "   escreva("], ["g", 3], ["t", ")"]],
            [["g", 4]],
        ],
        "gabarito": {"1": "inteiro", "2": "*", "3": "total", "4": "fimalgoritmo"},
        "opcoes": ["inteiro", "real", "*", "+", "-", "total", "preco", "fimalgoritmo"],
    },
]

# ─── SESSION STATE ────────────────────────────────────────────────────────────

def init():
    defaults = {
        "tela": "menu",           # "menu" | "nome_portugol" | "quiz_portugol" | "resultado_ex_portugol" | "final_portugol"
                                   # | "nome_operacoes" | "quiz_operacoes" | "resultado_ex_operacoes" | "final_operacoes"
        "nome_aluno": "",
        # Portugol
        "ex_idx_p": 0,
        "respostas_ex_p": [{} for _ in EXERCISES_PORTUGOL],
        "resultados_ex_p": [None for _ in EXERCISES_PORTUGOL],
        "acertos_ex_p": [0] * len(EXERCISES_PORTUGOL),
        # Operações
        "ex_idx_o": 0,
        "respostas_ex_o": [{} for _ in EXERCISES_OPERACOES],
        "resultados_ex_o": [None for _ in EXERCISES_OPERACOES],
        "acertos_ex_o": [0] * len(EXERCISES_OPERACOES),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def render_quiz(exercises, idx_key, respostas_key, resultados_key, acertos_key, fase_result, fase_final, fase_quiz):
    exercises_list = exercises
    idx      = st.session_state[idx_key]
    ex       = exercises_list[idx]
    gabarito = ex["gabarito"]
    opcoes   = ex["opcoes"]
    verificado = st.session_state[resultados_key][idx] is not None

    st.markdown(f"### Exercício {idx+1}/{len(exercises_list)} — {ex['titulo']}")
    if st.session_state.nome_aluno:
        st.markdown(f"<div style='color:#8b949e;font-size:.85rem;margin-bottom:.5rem'>👤 {st.session_state.nome_aluno}</div>", unsafe_allow_html=True)

    # Indicador de passos
    dots = '<div class="step-indicator">'
    for i in range(len(exercises_list)):
        cls = "done" if i < idx else ("active" if i == idx else "")
        dots += f'<div class="step-dot {cls}"></div>'
    dots += '</div>'
    st.markdown(dots, unsafe_allow_html=True)

    if ex.get("instrucao"):
        st.markdown(f"""<div style="background:#1c2128;border-left:3px solid #58a6ff;border-radius:6px;
            padding:.6rem 1rem;color:#8b949e;font-size:.85rem;margin-bottom:.8rem">{ex['instrucao']}</div>""",
            unsafe_allow_html=True)

    st.markdown('<div class="code-block">', unsafe_allow_html=True)

    for linha in ex["linhas"]:
        gaps_na_linha = [str(val) for tipo, val in linha if tipo == "g"]
        n_gaps = len(gaps_na_linha)

        if n_gaps == 0:
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
                        gid = str(val)
                        resp = st.session_state[respostas_key][idx].get(gid, "??")
                        ok   = st.session_state[resultados_key][idx].get(gid, False)
                        certo = gabarito[gid]
                        cls  = "gap-correct" if ok else "gap-wrong"
                        hint = "" if ok else f'<span class="gap-wrong-hint">✓ {certo}</span>'
                        html_row += f'<span class="{cls}">{resp}{hint}</span>'
                html_row += '</div>'
                st.markdown(html_row, unsafe_allow_html=True)
            else:
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
                            key = f"gap_{idx_key}_{idx}_{gid}"
                            opcoes_gap = ["— escolha —"] + opcoes
                            atual = st.session_state[respostas_key][idx].get(gid)
                            idx_atual = (opcoes_gap.index(atual) if atual and atual in opcoes_gap else 0)
                            escolha = st.selectbox(
                                label=f"gap{gid}",
                                options=opcoes_gap,
                                index=idx_atual,
                                key=key,
                                label_visibility="collapsed"
                            )
                            if escolha != "— escolha —":
                                st.session_state[respostas_key][idx][gid] = escolha
                            elif gid in st.session_state[respostas_key][idx]:
                                del st.session_state[respostas_key][idx][gid]
                    col_i += 1

    st.markdown('</div>', unsafe_allow_html=True)

    # Resultado do exercício
    if st.session_state.tela == fase_result:
        resultados = st.session_state[resultados_key][idx]
        acertos    = st.session_state[acertos_key][idx]
        total      = len(gabarito)
        cor = "#3fb950" if acertos == total else ("#f0883e" if acertos >= total // 2 else "#f85149")
        st.markdown(f"""
        <div style="text-align:center;padding:10px;border-radius:8px;
             color:{cor};background:{cor}18;border:1px solid {cor}44;
             font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;margin-bottom:.8rem">
            🎯 {acertos}/{total} acertos neste exercício
        </div>""", unsafe_allow_html=True)

        is_last = idx == len(exercises_list) - 1
        label   = "Ver Resultado Final 🏁" if is_last else "Próximo Exercício →"
        if st.button(label, use_container_width=True):
            if is_last:
                st.session_state.tela = fase_final
            else:
                st.session_state[idx_key] += 1
                st.session_state.tela = fase_quiz
            st.rerun()
        st.stop()

    # Botões de ação
    st.markdown("---")
    col1, col2 = st.columns([3, 1])

    respostas_atuais = st.session_state[respostas_key][idx]
    todas_preenchidas = all(str(k) in respostas_atuais for k in gabarito)

    with col1:
        if st.button("✅ Verificar Respostas", use_container_width=True, disabled=not todas_preenchidas):
            res = {k: (respostas_atuais.get(k) == v) for k, v in gabarito.items()}
            acertos = sum(1 for v in res.values() if v)
            st.session_state[resultados_key][idx] = res
            st.session_state[acertos_key][idx]    = acertos
            st.session_state.tela = fase_result
            st.rerun()

    with col2:
        if st.button("🗑 Limpar", use_container_width=True):
            st.session_state[respostas_key][idx] = {}
            st.rerun()

    if not todas_preenchidas:
        faltam = len(gabarito) - len(respostas_atuais)
        st.markdown(f"<div style='color:#8b949e;font-size:.78rem;margin-top:.3rem'>⚠️ Preencha ainda {faltam} lacuna(s) para verificar.</div>", unsafe_allow_html=True)


def render_final(exercises, acertos_key, nome):
    total_lac = sum(len(ex["gabarito"]) for ex in exercises)
    total_ac  = sum(st.session_state[acertos_key])
    emoji = "🏆" if total_ac == total_lac else ("👍" if total_ac >= total_lac // 2 else "📚")
    msg   = ("Perfeito! Você domina o conteúdo!" if total_ac == total_lac else
             "Muito bem! Continue praticando!" if total_ac >= total_lac // 2 else
             "Continue estudando, você vai melhorar!")
    st.markdown(f"""
    <div class="score-box">
        <div style="font-size:3rem">{emoji}</div>
        <div style="font-size:1.1rem;color:#8b949e;margin-bottom:.3rem">{nome}</div>
        <div class="score-number">{total_ac}/{total_lac}</div>
        <div style="color:#8b949e;margin-top:.5rem;font-size:1rem">{msg}</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    for i, ex in enumerate(exercises):
        ac  = st.session_state[acertos_key][i]
        tot = len(ex["gabarito"])
        cor = "#3fb950" if ac == tot else ("#f0883e" if ac >= tot // 2 else "#f85149")
        st.markdown(f"- **Ex {i+1}** — {ex['titulo']}: <span style='color:{cor}'>{ac}/{tot}</span>", unsafe_allow_html=True)

# ─── TELA: MENU ───────────────────────────────────────────────────────────────

if st.session_state.tela == "menu":
    st.markdown('<div class="menu-title">Atividades Aula</div>', unsafe_allow_html=True)
    st.markdown("---")

    col_a, col_b = st.columns(1), None

    if st.button("💻  Quiz Portugol", use_container_width=True):
        st.session_state.tela = "nome_portugol"
        st.rerun()

    if st.button("🔢  Operações Básicas", use_container_width=True):
        st.session_state.tela = "nome_operacoes"
        st.rerun()

    st.stop()

# ─── TELA: NOME ───────────────────────────────────────────────────────────────

if st.session_state.tela in ("nome_portugol", "nome_operacoes"):
    titulo = "💻 Quiz Portugol" if st.session_state.tela == "nome_portugol" else "🔢 Operações Básicas"
    proxima = "quiz_portugol" if st.session_state.tela == "nome_portugol" else "quiz_operacoes"

    st.markdown(f'<div class="quiz-title">{titulo}</div>', unsafe_allow_html=True)
    st.markdown('<div class="quiz-subtitle">Bem-vindo! Informe seu nome para começar.</div>', unsafe_allow_html=True)
    st.markdown("---")
    nome = st.text_input("👤 Seu nome", placeholder="Digite seu nome completo...", value=st.session_state.nome_aluno)
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("▶ Iniciar", use_container_width=True, disabled=not nome.strip()):
            st.session_state.nome_aluno = nome.strip()
            st.session_state.tela = proxima
            st.rerun()
    with col2:
        if st.button("← Voltar", use_container_width=True):
            st.session_state.tela = "menu"
            st.rerun()
    st.stop()

# ─── TELA: QUIZ PORTUGOL ──────────────────────────────────────────────────────

if st.session_state.tela in ("quiz_portugol", "resultado_ex_portugol"):
    st.markdown('<div class="quiz-title">💻 Quiz Portugol</div>', unsafe_allow_html=True)
    render_quiz(
        EXERCISES_PORTUGOL,
        "ex_idx_p", "respostas_ex_p", "resultados_ex_p", "acertos_ex_p",
        "resultado_ex_portugol", "final_portugol", "quiz_portugol"
    )
    st.stop()

# ─── TELA: RESULTADO FINAL PORTUGOL ──────────────────────────────────────────

if st.session_state.tela == "final_portugol":
    st.markdown('<div class="quiz-title">💻 Quiz Portugol</div>', unsafe_allow_html=True)
    render_final(EXERCISES_PORTUGOL, "acertos_ex_p", st.session_state.nome_aluno)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Refazer Quiz", use_container_width=True):
            st.session_state.ex_idx_p = 0
            st.session_state.respostas_ex_p = [{} for _ in EXERCISES_PORTUGOL]
            st.session_state.resultados_ex_p = [None for _ in EXERCISES_PORTUGOL]
            st.session_state.acertos_ex_p = [0] * len(EXERCISES_PORTUGOL)
            st.session_state.tela = "quiz_portugol"
            st.rerun()
    with col2:
        if st.button("🏠 Menu Principal", use_container_width=True):
            st.session_state.tela = "menu"
            st.rerun()
    st.stop()

# ─── TELA: QUIZ OPERAÇÕES ─────────────────────────────────────────────────────

if st.session_state.tela in ("quiz_operacoes", "resultado_ex_operacoes"):
    st.markdown('<div class="quiz-title">🔢 Operações Básicas</div>', unsafe_allow_html=True)
    render_quiz(
        EXERCISES_OPERACOES,
        "ex_idx_o", "respostas_ex_o", "resultados_ex_o", "acertos_ex_o",
        "resultado_ex_operacoes", "final_operacoes", "quiz_operacoes"
    )
    st.stop()

# ─── TELA: RESULTADO FINAL OPERAÇÕES ─────────────────────────────────────────

if st.session_state.tela == "final_operacoes":
    st.markdown('<div class="quiz-title">🔢 Operações Básicas</div>', unsafe_allow_html=True)
    render_final(EXERCISES_OPERACOES, "acertos_ex_o", st.session_state.nome_aluno)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Refazer Quiz", use_container_width=True):
            st.session_state.ex_idx_o = 0
            st.session_state.respostas_ex_o = [{} for _ in EXERCISES_OPERACOES]
            st.session_state.resultados_ex_o = [None for _ in EXERCISES_OPERACOES]
            st.session_state.acertos_ex_o = [0] * len(EXERCISES_OPERACOES)
            st.session_state.tela = "quiz_operacoes"
            st.rerun()
    with col2:
        if st.button("🏠 Menu Principal", use_container_width=True):
            st.session_state.tela = "menu"
            st.rerun()
    st.stop()
