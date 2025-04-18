def generate_visualizations():
    

    import os
    import pandas as pd
    import re
    import matplotlib.pyplot as plt
    import plotly.express as px

    reports_folder = "reports"
    report_files = [f for f in os.listdir(reports_folder) if f.startswith("alerts_") and f.endswith(".txt")]
    report_files.sort(reverse=True)
    latest_report = os.path.join(reports_folder, report_files[0])
    print(f"📄 Fichier analysé : {latest_report}")

    data = []
    with open(latest_report, 'r') as f:
        for line in f:
            match = re.match(r"\[(.*?)\] (.*?) -> (.*)", line.strip())
            if match:
                level, rule, log = match.groups()
                data.append({'level': level.upper(), 'rule': rule, 'log': log})

    df = pd.DataFrame(data)

    #  bar_rules.html
    rule_counts = df['rule'].value_counts().reset_index()
    rule_counts.columns = ['rule', 'count']
    fig1 = px.bar(rule_counts, x='rule', y='count', title="📊 Alertes par règle", text='count')
    fig1.update_traces(marker_color='indigo', textposition='outside')
    fig1.update_layout(xaxis_tickangle=-45)
    fig1.write_html("reports/bar_rules.html")
    print("✅ Graphique 'bar_rules.html' généré")

    #  treemap_gravite_rules.html
    df_grouped = df.groupby(['level', 'rule']).size().reset_index(name='count')
    fig2 = px.treemap(df_grouped, path=['level', 'rule'], values='count',
                    title="🌳 Répartition des alertes par gravité et règle",
                    color='level', color_discrete_sequence=px.colors.qualitative.Bold)
    fig2.write_html("reports/treemap_gravite_rules.html")
    print("✅ Graphique 'treemap_gravite_rules.html' généré")
