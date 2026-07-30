---
title: L'intelligence du regard
keywords:
- Perception visuelle
- Anatomie
- Modélisation neurale
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
  <meta name="dc.title" content="L&#39;intelligence du regard" />
  <meta name="citation_title" content="L&#39;intelligence du regard" />
  <meta property="og:title" content="L&#39;intelligence du regard" />
  <meta property="twitter:title" content="L&#39;intelligence du regard" />
  <meta name="dc.date" content="2026-07-08" />
  <meta name="citation_publication_date" content="2026-07-08" />
  <meta property="article:published_time" content="2026-07-08" />
  <meta name="dc.modified" content="2026-07-30T07:02:15+00:00" />
  <meta property="article:modified_time" content="2026-07-30T07:02:15+00:00" />
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
  <link rel="alternate" type="text/html" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/6bf8d48dbfa268592aa6b980affce494efb82bf9/" />
  <meta name="manubot_html_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/6bf8d48dbfa268592aa6b980affce494efb82bf9/" />
  <meta name="manubot_pdf_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/6bf8d48dbfa268592aa6b980affce494efb82bf9/manuscript.pdf" />
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
([permalink](https://laurentperrinet.github.io/2026-07_intelligence-regard/v/6bf8d48dbfa268592aa6b980affce494efb82bf9/))
was automatically generated
from [laurentperrinet/2026-07_intelligence-regard@6bf8d48](https://github.com/laurentperrinet/2026-07_intelligence-regard/tree/6bf8d48dbfa268592aa6b980affce494efb82bf9)
on July 30, 2026.
</em></small>

Published: July 8, 2026


## Authors



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


## Abstract {.page_break_before}




Et si votre cerveau remodelait l’espace qui vous entoure à votre insu ? Intuitivement, nous pensons que notre vision reflète fidèlement le monde. Pourtant, l’image projetée sur la rétine est très inégale. Au centre, la précision est maximale. En périphérie, la vision devient floue et moins sensible aux couleurs. Comment le cerveau reconstruit-il alors une perception visuelle cohérente ?

Comprendre ce mécanisme est un enjeu majeur. Cela éclaire le fonctionnement de la vision. Cela aide aussi à mieux diagnostiquer certaines maladies oculaires. Cela inspire enfin des systèmes d’intelligence artificielle plus sobres en énergie. En tant que chercheur en neurosciences computationnelles, j’étudie comment le cerveau assemble des informations visuelles partielles. Voici ce que les recherches récentes révèlent sur le rôle décisif de l’organisation spatiale de la rétine.

# La rétine, organe sensible de la vision

La vision semble si naturelle. Il suffit d’ouvrir les yeux pour percevoir le monde. Pourtant, derrière cette apparente simplicité se cache un mécanisme d’une grande complexité. Ce mystère intrigue les scientifiques depuis des siècles. Dès le XIe siècle, Ibn al-Haytham, aussi appelé Alhazen, pose les bases d’une théorie moderne de l’optique. Il montre comment la lumière traverse l’œil pour former une image sur la rétine. Plus tard, Léonard de Vinci s’appuie sur ces travaux. Le processus visuel commence dans une fine couche de cellules au fond de l’œil: la rétine. Elle capte la lumière focalisée par l’œil. En quelques millisecondes, elle la transforme en signaux nerveux que le cerveau peut interpréter. Une propriété remarquable du système visuel est la conservation de cette organisation spatiale dans plusieurs aires cérébrales. Des neurones voisins dans une aire visuelle correspondent à des points proches du champ visuel. Cette cartographie, appelée rétinotopie, structure une grande partie du traitement visuel.

La rétine ne traite cependant pas toute l’image de manière uniforme. Elle privilégie une petite zone centrale, la fovéa, située dans la macula. Pour donner un ordre de grandeur, la macula couvre un angle visuel proche de celui de la taille du pouce tendu à bout de bras. Bien qu’elle ne représente qu’une petite portion d’un champ visuel large comme un hémicycle, elle mobilise environ un quart des fibres du nerf optique (voir FIGURE RETINE). Cette concentration de ressources explique la précision des détails et des couleurs autour du point de fixation. En effet, la macula contient surtout des cônes, des cellules sensibles aux couleurs. La périphérie rétinienne contient surtout des bâtonnets, plus efficaces en faible lumière mais moins sensibles aux couleurs. Un paradoxe apparaît alors: si la périphérie distingue mal les couleurs, pourquoi notre perception du monde paraît-elle globalement uniforme et colorée ? Une partie de la réponse tient au mouvement permanent du regard. En ce moment même, vos yeux se déplacent pour fixer ces mots l’un après l’autre. Selon la position du regard, une information peut se révéler ou se cacher (voir FIGURE ILLUSION).

Cette spécialisation centrale de la rétine n’est pas propre à l’humain. On la retrouve chez de nombreux mammifères, avec des adaptations spécifiques selon les espèces. Chez le chat, les photorécepteurs sont davantage concentrés le long de l’axe horizontal. Chez le lapin ou la souris, leur répartition est plus uniforme. Certaines espèces vont plus loin: faucons et certains dauphins possèdent deux fovéas par œil, l’une pour la vision frontale précise, l’autre pour une perception latérale optimisée.

# Un enjeu clinique crucial

En quoi est‑il utile d’étudier la géométrie de la rétine ? Cet aspect est essentiel pour comprendre de nombreuses pathologies visuelles. La dégénérescence maculaire liée à l’âge (DMLA) est l’un des exemples les plus marquants. Elle affecte gravement la macula décrite plus haut. Avec le vieillissement de la population, elle est devenue la première cause de malvoyance chez les plus de 50 ans. Son effet est particulièrement délétère. Elle rend invisibles les objets placés au centre du regard, comme les visages ou les lettres. La vie quotidienne peut alors être fortement perturbée. Avec le Dr Kevin Mairot, à l’AP‑HM, nous utilisons des outils d’intelligence artificielle pour détecter des formes rares de DMLA. Dans certains contextes, ces outils atteignent une efficacité supérieure à celle des spécialistes. L’objectif n’est pas de remplacer le praticien. Il s’agit de l’aider à décider, en complément de l’ensemble des informations sur le patient.

D’autres pathologies visuelles existent. Elles sont nombreuses, diverses et souvent méconnues. Cette méconnaissance peut entraîner une errance médicale et retarder la prise en charge. Certaines formes de la maladie d’Alzheimer touchent spécifiquement les voies visuelles. L’atteinte peut s’étendre de la rétine jusqu’au cortex occipito‑pariétal, qui inclut des aires visuelles primaires essentielles à la perception. Ces atteintes peuvent altérer la reconnaissance des visages et des émotions. Les conséquences sociales sont souvent sévères. Certaines formes affectent surtout le champ périphérique. La vision se rétrécit alors autour du point de fixation, avec un « effet tunnel ». Le Dr Lejla Koric, à l’AP‑HM, mène des études novatrices pour diagnostiquer précocement ces formes à partir de réponses comportementales visuelles, afin de traiter ces troubles mieux et plus tôt.

Les pathologies rétiniennes n’affectent pas seulement la perception. Elles peuvent aussi dégrader le contrôle des mouvements oculaires. La rétinotopie humaine concentre de grandes ressources autour de la macula et du point de fixation, lui-même piloté par le regard. Quand cette zone dégénère, le contrôle oculomoteur peut devenir inefficace. On peut observer des saccades involontaires ou un mauvais suivi d’objets en mouvement.Ces troubles compliquent la lecture et la reconnaissance des visages. Le retentissement personnel peut être important. Des solutions thérapeutiques innovantes existent. Elles combinent, par exemple, casques de réalité virtuelle et capteurs de position du regard. Ces dispositifs peuvent soutenir une rééducation du contrôle oculomoteur [Castet & Calabrese].

# L'outil de la modélisation

Pour comprendre le rôle de la rétinotopie dans la vision, la modélisation est un outil clé. Le principe est simple. Nous construisons un système visuel artificiel qui reproduit des caractéristiques humaines. Nous pouvons ensuite modifier certains éléments et observer leur rôle dans l’ensemble.

Nous avons utilisé un modèle appelé ConvNeXt, l’un des modèles de référence actuels en vision par ordinateur. Ce type de réseau classe des images arbitraires dans des catégories, comme « poisson rouge » ou « clavier ». Nous avons comparé ses performances sur des images classiques et sur des images transformées par la rétinotopie humaine. Le résultat est surprenant. Le réseau reste efficace avec ces images déformées. Il acquiert même de nouvelles capacités, comme la détection d’un animal camouflé dans une scène visuelle (cf FIGURE MODELE).

Cette capacité de localisation ouvre des perspectives en IA et en neurosciences. L’usage des capteurs visuels augmente rapidement, des téléphones intelligents aux voitures connectées. Chaque capteur impose des traitements de plus en plus complexes. Les coûts énergétiques augmentent donc fortement. En priorisant les pixels autour d’une région d’intérêt, on peut réduire significativement ces coûts de traitement. Ces approches peuvent aussi accélérer la réponse des systèmes, ce qui est crucial pour la nouvelle génération de voitures.

Cette voie de recherche ouvre aussi un nouvel axe en neurosciences de la vision. Notre perception paraît uniforme. Pourtant, elle est concentrée autour du point de fixation. En périphérie, les sensations sont plus floues et moins colorées. Comment détecter, dans cette zone dégradée, qu’un nouveau point d’intérêt mérite un déplacement du regard ?

Cette question met en lumière le lien étroit entre la sensation rétinienne et le système oculomoteur. Elle encourage une nouvelle génération de modèles. Ces modèles doivent pouvoir agir sur leur environnement, et pas seulement l’analyser. Cette capacité reste encore largement sous-exploitée dans les systèmes actuels d’intelligence artificielle.

# Conclusion

La géométrie de la rétine n’est pas celle de notre perception. Ce décalage ne fragilise pas notre compréhension de la vision. Il la rend plus précise. En révélant ce « miroir déformant », nous progressons dans l’analyse d’un système particulièrement complexe.

Nos résultats soulignent un point central. Une rétinotopie fovéée n’est vraiment efficace que si le regard peut explorer activement la scène visuelle. La sensation et l’action sont donc indissociables. C’est précisément dans ce couplage que se situent les prochaines découvertes sur l’intelligence de la vision et du regard.

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

