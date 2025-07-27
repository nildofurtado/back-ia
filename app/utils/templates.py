from datetime import datetime


def transcription_finalized_template(summary: str) -> str:

    participantes = ''.join(
        f"<li>{p.get('nome', 'Desconhecido')} - {p.get('função', 'undefined')}</li>"
        for p in summary.get('participants', [])
    )

    empresas = ''.join(f"<li>{c}</li>" for c in summary.get('companies', []))
    topicos = ''.join(f"<li>{t}</li>" for t in summary.get('main_topics', []))

    capitulos = ''.join(
        f"<li><strong>{cap.get('capítulo', 'Sem título')}:</strong> {cap.get('tópico', 'Sem conteúdo')}</li>"
        for cap in summary.get('Chapters and topics', [])
    )

    perguntas = ''.join(f"<li>{q}</li>" for q in summary.get('Key Questions', []))

    acoes = ''.join(
        f"<li><strong>{a.get('ação', 'undefined')}</strong> - "
        f"Responsável: {a.get('responsável', 'undefined')} | Prazo: {a.get('prazo', 'undefined')}</li>"
        for a in summary.get('actions or Tasks', [])
    )

    passos = ''.join(f"<li>{s}</li>" for s in summary.get('next_steps', []))
    anotacoes = ''.join(f"<li>{n}</li>" for n in summary.get('Notepad', []))

    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>[ Resumo da Reunião ]</h2>
        <p><strong>Resumo:</strong> {summary.get('summary', 'Sem resumo disponível')}</p>

        <h3>Participantes</h3>
        <ul>{participantes or "<li>Sem participantes identificados</li>"}</ul>

        <h3>Empresas Mencionadas</h3>
        <ul>{empresas or "<li>Nenhuma empresa mencionada</li>"}</ul>

        <h3>Tópicos Principais</h3>
        <ul>{topicos or "<li>Nenhum tópico identificado</li>"}</ul>

        <h3>Capítulos e Tópicos</h3>
        <ul>{capitulos or "<li>Nenhum capítulo/tópico</li>"}</ul>

        <h3>Perguntas-chave</h3>
        <ul>{perguntas or "<li>Nenhuma pergunta encontrada</li>"}</ul>

        <h3>Ações ou Tarefas</h3>
        <ul>{acoes or "<li>Nenhuma ação registrada</li>"}</ul>

        <h3>Próximos Passos</h3>
        <ul>{passos or "<li>Sem próximos passos definidos</li>"}</ul>

        <h3>Anotações</h3>
        <ul>{anotacoes or "<li>Sem anotações</li>"}</ul>
    </body>
    </html>
    """
