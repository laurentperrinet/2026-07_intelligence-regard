---
title: 'L''intelligence du regard : comment le cerveau reconstruit un monde cohérent à partir d’une image déformée'
keywords:
- perception visuelle
- rétinotopie
- neurosciences
- santé visuelle
- intelligence artificielle
- modélisation
lang: fr-FR
date-meta: '2026-07-08'
author-meta:
- Laurent U Perrinet
header-includes: |
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta property="og:type" content="article" />
  <meta name="dc.title" content="L&#39;intelligence du regard : comment le cerveau reconstruit un monde cohérent à partir d’une image déformée" />
  <meta name="citation_title" content="L&#39;intelligence du regard : comment le cerveau reconstruit un monde cohérent à partir d’une image déformée" />
  <meta property="og:title" content="L&#39;intelligence du regard : comment le cerveau reconstruit un monde cohérent à partir d’une image déformée" />
  <meta property="twitter:title" content="L&#39;intelligence du regard : comment le cerveau reconstruit un monde cohérent à partir d’une image déformée" />
  <meta name="dc.date" content="2026-07-08" />
  <meta name="citation_publication_date" content="2026-07-08" />
  <meta property="article:published_time" content="2026-07-08" />
  <meta name="dc.modified" content="2026-08-25T07:08:57+00:00" />
  <meta property="article:modified_time" content="2026-08-25T07:08:57+00:00" />
  <meta name="dc.language" content="fr-FR" />
  <meta name="citation_language" content="fr-FR" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Laurent U Perrinet" />
  <meta name="citation_author_institution" content="Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université" />
  <meta name="citation_author_orcid" content="0000-0002-9536-010X" />
  <link rel="canonical" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/" />
  <meta property="og:url" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/" />
  <meta property="twitter:url" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/" />
  <meta name="citation_fulltext_html_url" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/" />
  <meta name="citation_pdf_url" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/aad6328a028f5810ffaeb394a5c5260392d10dfc/" />
  <meta name="manubot_html_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/aad6328a028f5810ffaeb394a5c5260392d10dfc/" />
  <meta name="manubot_pdf_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/aad6328a028f5810ffaeb394a5c5260392d10dfc/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://laurentperrinet.github.io/2026-07_intelligence-regard/v/aad6328a028f5810ffaeb394a5c5260392d10dfc/))
was automatically generated
from [laurentperrinet/2026-07_intelligence-regard@aad6328](https://github.com/laurentperrinet/2026-07_intelligence-regard/tree/aad6328a028f5810ffaeb394a5c5260392d10dfc)
on August 25, 2026.
</em></small>

Published: July 8, 2026


## Auteur



+ **Laurent U Perrinet**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-9536-010X](https://orcid.org/0000-0002-9536-010X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [laurentperrinet](https://github.com/laurentperrinet)
    · ![Mastodon icon](images/mastodon.svg){.inline_icon width=16 height=16}
    [\@laurentperrinet@neuromatch.social](https://neuromatch.social/@laurentperrinet)
    <br>
  <small>
     Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université
  </small>


::: {#correspondence}
✉ — Correspondence possible via [GitHub Issues](https://github.com/laurentperrinet/2026-07_intelligence-regard/issues)

:::


## Résumé {.page_break_before}




*Nous avons l’impression de voir un monde continu, net et coloré. Pourtant, l’image captée par la rétine n'est pas uniforme : ultra-précise au centre, plus floue et moins riche en couleurs en périphérie. Comprendre ce processus permet de mieux comprendre et diagnostiquer certaines pathologies visuelles et inspire des approches plus sobres en intelligence artificielle.*

Et si votre cerveau remodelait l’espace qui vous entoure à votre insu ? Intuitivement, nous pensons que notre vision reflète fidèlement le monde. Pourtant, l’image formée sur la rétine est loin d'être uniforme! Au centre, la précision est maximale. En périphérie, la vision devient floue et moins sensible aux couleurs. Comment le cerveau parvient-il alors à reconstruire la scène cohérente et apparamment uniforme que nous percevons ?

Comprendre ce mécanisme est un enjeu majeur. Il éclaire sur le fonctionnement de la vision. Il aide aussi à mieux diagnostiquer certaines maladies oculaires. Il inspire enfin des systèmes d’intelligence artificielle plus sobres en énergie. En tant que chercheur en neurosciences computationnelles, j’étudie comment le cerveau assemble des informations visuelles partielles pour produire une perception cohérente. Voici ce que les recherches récentes révèlent sur le rôle décisif de l’organisation spatiale de la rétine.

## Ce que la rétine voit vraiment

La vision semble si naturelle. Il suffit d’ouvrir les yeux pour percevoir le monde. Pourtant, derrière cette apparente simplicité se cache un mécanisme d’une grande complexité qui intrigue les scientifiques depuis des siècles. Dès le XIe siècle, Ibn al-Haytham, aussi appelé Alhazen, pose les bases d’une théorie moderne de l’optique. Il montre comment la lumière traverse l’œil pour former une image sur la rétine. Plus tard, Léonard de Vinci s’inspirera de ces travaux pour ses propres recherches sur la vision. Le processus visuel commence dans une fine couche de cellules au fond de l’œil : la rétine. Elle capte la lumière focalisée par l’œil. En quelques millisecondes, elle la transforme en signaux nerveux que le cerveau peut interpréter. Une propriété remarquable du système visuel est la conservation de cette organisation spatiale dans plusieurs aires cérébrales. Dans le cerveau, les neurones voisins traitent des zones voisines de ce que nous voyons. Cette correspondance entre le cerveau et le champ visuel, appelée *rétinotopie*, est une clé de notre perception.

La rétine ne traite cependant pas toute l’image de manière uniforme. En ce moment même, vos yeux se déplacent pour fixer ces mots l’un après l’autre. Selon l’endroit où vous regardez, certaines informations deviennent visibles, tandis que d’autres disparaissent (voir Figure @fig:pale-blue). La vision privilégie une petite zone centrale, la fovéa, située dans la macula. Pour donner un ordre de grandeur, la macula couvre un angle visuel proche de celui d’un pouce tendu à bout de bras. Bien qu’elle ne représente qu’une petite portion du champ visuel qui est lui large comme un hémicycle, elle mobilise pourtant environ un quart des fibres du nerf optique (voir FIGURE RETINE). Cette concentration de ressources explique la précision des détails et des couleurs autour du point de fixation. Cette différence s’explique simplement : la macula contient surtout des cônes, des cellules sensibles aux couleurs. La périphérie rétinienne contient surtout des bâtonnets, plus efficaces en faible lumière mais moins sensibles aux couleurs. Un paradoxe apparaît alors : si la périphérie distingue mal les couleurs, pourquoi notre perception du monde paraît-elle globalement uniforme et colorée ? 

Explorons alors d'autres espèces. En effet, cette spécialisation centrale de la rétine n’est pas propre à l’humain. On la retrouve chez de nombreux mammifères, avec des adaptations spécifiques. Chez le chat, les photorécepteurs sont concentrés le long de l’axe horizontal. Chez le lapin ou la souris, leur répartition est plus uniforme. Certaines espèces poussent cette spécialisation encore plus loin : les faucons et certains dauphins possèdent deux fovéas par œil, l’une pour la vision frontale précise, l’autre pour une perception latérale optimisée. Pourquoi? Une partie de la réponse tient aux niches écologiques de chaque espèce et au mouvement permanent du regard tel qu'il s'y est adapté. 

![
**L'œil voit différemment dans et hors la fovea.** Ces différents points semblent similaires pourtant celui sur lequel on pose son œil a une couleur différente, qui s'évanonouie lorsque l'on regarde ailleurs. Cet effet dépend des [paramètres réglant la couleur des points et du fond](https://laurentperrinet.github.io/sciblog/posts/2026-07-31-pale-blue-dots.html) et auxquelles la fovea est particulièrement plus sensible par rapport à la périphérie.](https://raw.githubusercontent.com/laurentperrinet/sciblog/refs/heads/master/files/2026-07-31-pale-blue-dots_random.svg?sanitize=true "Pale blue dots"){#fig:pale-blue height=6cm .white}


## Pourquoi cette géométrie est cruciale en clinique

En quoi est‑il utile d’étudier la géométrie de la rétine ? Comprendre cette organisation permet d’éclairer de nombreuses pathologies visuelles. La dégénérescence maculaire liée à l’âge (DMLA) est l’un des exemples les plus marquants. Elle affecte gravement la macula décrite plus haut. Avec le vieillissement de la population, elle est devenue la première cause de malvoyance chez les plus de 50 ans. Son effet est particulièrement délétère. Elle rend flous ou illisibles les objets placés au centre du regard, comme les visages ou les lettres. La vie quotidienne peut alors être fortement perturbée. Avec le Dr Kevin Mairot, à l’AP‑HM, nous utilisons des outils d’intelligence artificielle pour détecter des formes rares de DMLA. Dans certains contextes, et selon les données disponibles, ces outils peuvent atteindre une efficacité comparable, voire supérieure, à celle de spécialistes. L’objectif n’est pas de remplacer le praticien, mais de l’épauler dans son diagnostic, en complément de l’ensemble des informations sur le patient.

D’autres pathologies visuelles existent. Elles sont nombreuses, diverses et souvent méconnues. Cette méconnaissance peut entraîner une errance médicale et retarder la prise en charge. Certaines formes de la maladie d’Alzheimer touchent spécifiquement les voies visuelles. L’atteinte peut s’étendre de la rétine jusqu’aux zones du cerveau responsables de la perception visuelle. Ces atteintes peuvent, par exemple, rendre difficile la reconnaissance d’un visage familier ou l’interprétation des expressions faciales. Les conséquences sociales sont souvent sévères. Certaines formes affectent surtout le champ périphérique. La vision se rétrécit alors autour du point de fixation, comme si l’on regardait à travers un tube : on ne voit plus que le centre, et tout le reste disparaît. C’est ce qu’on appelle l’« effet tunnel ». Le Dr Lejla Koric, à l’AP‑HM, mène des études novatrices pour diagnostiquer précocement ces formes à partir de réponses comportementales visuelles, afin de traiter ces troubles mieux et plus tôt.

Les pathologies rétiniennes n’affectent pas seulement la perception. Elles peuvent aussi dégrader le contrôle des mouvements oculaires. La rétinotopie humaine concentre de grandes ressources autour de la macula et du point de fixation, lui-même piloté par le regard. Quand cette zone dégénère, la capacité à diriger son regard peut être altérée. On peut observer des saccades involontaires ou un mauvais suivi d’objets en mouvement. Ces troubles compliquent la lecture et la reconnaissance des visages. Ces troubles peuvent avoir un retentissement majeur sur la vie quotidienne. Heureusement, des solutions thérapeutiques innovantes voient le jour. Elles combinent, par exemple, casques de réalité virtuelle et capteurs de position du regard. Ces dispositifs peuvent soutenir une rééducation du contrôle oculomoteur [Castet & Calabrese].

## Ce que la modélisation et l’IA permettent de tester

Pour comprendre le rôle de la rétinotopie dans la vision, la modélisation est un outil clé. Le principe est le suivant : nous construisons un système visuel artificiel qui reproduit des caractéristiques humaines. Nous modifions ensuite certains éléments pour observer leur rôle dans l’ensemble.

Nous avons utilisé un modèle appelé ConvNeXt, un modèle de référence actuel en vision par ordinateur. Ce réseau peut reconnaître et classer des images variées dans des catégories, comme « poisson rouge » ou « clavier ». Nous avons comparé ses performances sur des images classiques et sur des images transformées par la rétinotopie humaine. Un résultat notable apparaît. Le réseau conserve un niveau de performance élevé avec ces images déformées. Il montre aussi de nouvelles capacités, comme la détection d’un animal camouflé dans une scène visuelle (cf FIGURE MODELE).

Cette capacité à localiser des objets ouvre de nouvelles perspectives, tant en IA qu’en neurosciences. L’usage des capteurs visuels augmente rapidement, des téléphones intelligents aux voitures connectées. Chaque capteur impose des traitements de plus en plus complexes. Les coûts énergétiques augmentent donc fortement. En se concentrant sur les pixels autour d’une zone d’intérêt, on peut réduire significativement les coûts de traitement. Cette approche est particulièrement utile pour les systèmes embarqués, comme les voitures autonomes. Ces approches peuvent aussi accélérer la réponse des systèmes, ce qui est crucial pour cette nouvelle génération de voitures.

Cette voie de recherche ouvre aussi un nouvel axe en neurosciences de la vision. Notre perception paraît uniforme. Pourtant, elle est concentrée autour du point de fixation. En périphérie, les sensations sont plus floues et moins colorées. Comment détecter, dans cette zone floue, un point d’intérêt justifiant un déplacement du regard ?

Cette question révèle le lien étroit entre ce que voit la rétine et le système qui contrôle les mouvements des yeux. Elle encourage une nouvelle génération de modèles. Ces modèles doivent pouvoir agir sur leur environnement, et pas seulement l’analyser. Or, cette capacité reste encore largement sous-exploitée dans l’IA actuelle.

## Ce que cela change pour comprendre l’intelligence du regard

La géométrie de la rétine n’est pas celle de notre perception. Loin de fragiliser notre compréhension, ce décalage la rend au contraire plus précise. En révélant ce « miroir déformant » — où la rétine capte une image inégale mais le cerveau en fait une perception uniforme — nous progressons dans l’analyse d’un système particulièrement complexe.

Nos travaux mettent en lumière un point clé : cette spécialisation centrale de la rétine semble pleinement efficace lorsque le regard explore activement la scène visuelle. La perception et les mouvements des yeux apparaissent donc étroitement liés. C’est dans ce couplage entre perception et action que se situent probablement les prochaines avancées, comme le développement de prothèses visuelles intelligentes ou de robots capables de voir comme nous. De nouvelles avancées passionnantes sont attendues dans ce domaine.

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

