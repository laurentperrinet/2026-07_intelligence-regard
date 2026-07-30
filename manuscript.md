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
  <meta name="dc.modified" content="2026-07-30T06:54:23+00:00" />
  <meta property="article:modified_time" content="2026-07-30T06:54:23+00:00" />
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
  <link rel="alternate" type="text/html" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e67c187872fa362fff890df90ac44a98b76f1b2d/" />
  <meta name="manubot_html_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e67c187872fa362fff890df90ac44a98b76f1b2d/" />
  <meta name="manubot_pdf_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e67c187872fa362fff890df90ac44a98b76f1b2d/manuscript.pdf" />
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
([permalink](https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e67c187872fa362fff890df90ac44a98b76f1b2d/))
was automatically generated
from [laurentperrinet/2026-07_intelligence-regard@e67c187](https://github.com/laurentperrinet/2026-07_intelligence-regard/tree/e67c187872fa362fff890df90ac44a98b76f1b2d)
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




Et si on vous disait que votre cerveau remodelait l’espace qui vous entoure sans que vous vous en rendiez compte ? Intuitivement, on pourrait croire que notre vision de l’espace reflète fidèlement sa représentation dans le cerveau. Pourtant, l’image projetée sur la rétine est très inégale: au centre, la précision est maximale ; en périphérie, la vision devient floue et moins sensible aux couleurs. Comment notre cerveau parvient-il alors à reconstruire l'image que nous percevons ?

Comprendre ce mécanisme est un enjeu majeur. Il éclaire le fonctionnement de la vision, aide à mieux diagnostiquer certaines maladies oculaires et inspire des systèmes d’intelligence artificielle plus sobres en énergie. En tant que chercheur en neurosciences computationnelles, j’étudie la manière dont le cerveau assemble ces informations visuelles partielles pour produire une perception cohérente. Voici ce que les recherches récentes révèlent sur le rôle décisif de l’organisation spatiale de la rétine.

# La rétine, organe sensible de la vision

La vision semble si naturelle. Il suffit d’ouvrir les yeux pour percevoir le monde. Pourtant, derrière cette apparente simplicité se cache un mécanisme d’une grande complexité. Ce mystère intrigue les scientifiques depuis des siècles. Dès le XIe siècle, Ibn al-Haytham, aussi appelé Alhazen, pose les bases d’une théorie moderne de l’optique. Il montre comment la lumière traverse l’œil pour former une image sur la rétine. Plus tard, Léonard de Vinci s’appuie sur ces travaux. Le processus visuel commence dans une fine couche de cellules au fond de l’œil: la rétine. Elle capte la lumière focalisée par l’œil. En quelques millisecondes, elle la transforme en signaux nerveux que le cerveau peut interpréter. Une propriété remarquable du système visuel est la conservation de cette organisation spatiale dans plusieurs aires cérébrales. Des neurones voisins dans une aire visuelle correspondent à des points proches du champ visuel. Cette cartographie, appelée rétinotopie, structure une grande partie du traitement visuel.

La rétine ne traite cependant pas toute l’image de manière uniforme. Elle privilégie une petite zone centrale, la fovéa, située dans la macula. Pour donner un ordre de grandeur, la macula couvre un angle visuel proche de celui de la taille du pouce tendu à bout de bras. Bien qu’elle ne représente qu’une petite portion d’un champ visuel large comme un hémicycle, elle mobilise environ un quart des fibres du nerf optique (voir FIGURE RETINE). Cette concentration de ressources explique la précision des détails et des couleurs autour du point de fixation. En effet, la macula contient surtout des cônes, des cellules sensibles aux couleurs. La périphérie rétinienne contient surtout des bâtonnets, plus efficaces en faible lumière mais moins sensibles aux couleurs. Un paradoxe apparaît alors: si la périphérie distingue mal les couleurs, pourquoi notre perception du monde paraît-elle globalement uniforme et colorée ? Une partie de la réponse tient au mouvement permanent du regard. En ce moment même, vos yeux se déplacent pour fixer ces mots l’un après l’autre. Selon la position du regard, une information peut se révéler ou se cacher (voir FIGURE ILLUSION).

Cette spécialisation centrale de la rétine n’est pas propre à l’humain. On la retrouve chez de nombreux mammifères, avec des adaptations spécifiques selon les espèces. Chez le chat, les photorécepteurs sont davantage concentrés le long de l’axe horizontal. Chez le lapin ou la souris, leur répartition est plus uniforme. Certaines espèces vont plus loin: faucons et certains dauphins possèdent deux fovéas par œil, l’une pour la vision frontale précise, l’autre pour une perception latérale optimisée.

# Un enjeu clinique crucial

En quoi est‑il utile d’étudier la géométrie de la rétine ? Tout d’abord, cet aspect de la vision humaine est essentiel pour comprendre les nombreuses pathologies qui peuvent affecter notre vision. L’une de ces pathologies est la dégénérescence maculaire liée à l’âge (DMLA), qui affecte gravement la macula que nous avons décrite ci‑dessus. Avec le vieillissement de la population, la DMLA est devenue la première cause de malvoyance chez les personnes de plus de 50 ans. Avec l’importance de la macula que nous avons soulignée, on comprend mieux pourquoi l’effet de cette maladie est particulièrement délétère : elle invisibilise tout objet placé au centre de notre regard (par exemple visages ou lettres), perturbant ainsi fortement et durablement la vie quotidienne. Avec le Dr Kevin Mairot de l’AP‑HM, nous utilisons les nouveaux outils d’intelligence artificielle pour détecter des formes rares de DMLA, avec une efficacité souvent supérieure à celle des spécialistes. L’objectif n’est bien sûr pas de remplacer le praticien, mais plutôt de l’aider dans son diagnostic en complément de l'ensemble des connaissances sur le patient.

Un riche inventaire d’autres pathologies visuelles existe : elles sont diverses et souvent méconnues, ce qui peut provoquer une errance médicale et retarder leur prise en charge. Par exemple, une forme de la maladie d’Alzheimer peut impacter spécifiquement les voies visuelles, depuis la rétine jusqu’au cortex occipito‑pariétal qui concentre les aires visuelle primaires et qui est essentiel à la perception visuelle. Une conséquence peut alors être une altération de la reconnaissance des visages et de leurs émotions, ce qui nuit gravement à la vie sociale. Une forme de cette pathologie affecte notamment le champ périphérique ; notre vision du monde se rétrécit alors autour du centre de notre regard, créant ce que l’on appelle un « effet tunnel ». Le docteur Lejla Koric, à l’AP‑HM, conduit des études novatrices pour diagnostiquer, à partir de réponses comportementales visuelles, de façon précoce ces formes de la maladie d’Alzheimer, afin de les traiter mieux et plus tôt.

Ainsi, les pathologies rétiniennes n'affectent pas seulement la perception visuelle mais peuvent aussi avoir des conséquences délétères sur notre contrôle du mouvement des yeux. En effet nous avons vu que la rétinotopie humaine concentre de grandes ressources à la macula qui se concentre autour du point de fixation, lui-même contrôlé par nos mouvements du regard. La dégénérescence de cette zone du champ visuel peut fortement perturber le contrôle de ce mouvement, générant par exemple des saccades involontaires ou un contrôle inefficace du suivi d'objets en mouvement. Ceci peut induire une difficulté à lire ou à reconnaître des visages, avec des impacts personnels délétères. Des solutions thérapeutiques innovantes peuvent être proposées, par exemple en utilisant des casques de réalité virtuelle couplés avec des détecteurs de la position du regard qui permettent de faciliter une rééducation du contrôle du regard. [Castet & Calabrese]

# L'outil de la modélisation

Afin de mieux comprendre le rôle de la rétinotopie dans la vision, un outil essentiel est la modélisation. C'est en construisant de toutes pièces un système visuel reproduisant efficacément les caractéristiques humaines que l'on peut alors manipuler certaines de ces pièces et comprendre leur rôle dans la mécanique globale. C'est ce que nous avons fait en utilisant le modèle convNext, qui est ce qui se fait de mieux actuellement en vision par ordinateur et intelligence artificielle pour identifier des classes (par exemple "poisson rouge" ou "clavier") dans des images arbitraires. Nous avons testé les capacités de ce réseau en lui présentant soit les images classiques, soit des images transformées par la rétinotopie humaine. De façon surprenante, le réseau reste efficace avec ces images déformées et mieux, il démontre de nouvelles capacités, comme celle de découvrir un animal camouflé dans une scène visuelle (cf FIGURE MODELE).

Cette nouvelle capacité de notre modèle à localiser des objets visuels constitue une porte ouverte à de nouveaux progrès aussi bien en IA qu'en neurosciences. En effet, l'utilisation de capteurs visuels suit une croissance exponentielle, depuis les téléphones intelligents aux voitures connectées, et chacun de ces capteurs requiert des traitements de plus en plus complexes. Ceci démultiplie les coûts énergétiques, ce qui rend critique le besoin de gérer au mieux leur consommation. En utilisant en priorité les pixels autour d'une région d'intérêt, on peut ainsi diviser les coûts de traitements d'un facteur significatif. De plus, ces systèmes peuvent permettre de répondre plus rapidement ce qui est crucial par exemple dans la nouvelle génération de voitures.

De façon complémentaire, cette voie de recherche soulève un nouvel axe de recherche en neurosciences de la vision. En effet notre perception de la scène visuelle semble uniforme et pourtant nous avons mis en évidence qu'elle est concentrée autour du point de fixation de notre regard. En contrepartie, nos sensations en périphérie sont fortement dégradées, floues et sans couleur. Comment alors détecter qu'il y aurait un nouveau point d'intérêt dans cette zone périphérique, c'est-à-dire qu'il y ait un intérêt à déplacer notre regard pour une nouvelle exploration de l'espace visuel ? Cette question révèle le lien intime entre la sensation produite par la rétine et l'ensemble du système oculomoteur qui nous permet de déplacer notre regard. Cette nouvelle perspective nous encourage à une nouvelle approche pour construire ce type de modèles en leur donnant la liberté d'agir sur le monde environnant, une capacité largement sous-exploitée dans les systèmes actuels d'intelligence artificielle.

# Conclusion

Pour conclure, en mettant en lumière que la géométrie de l’œil, l'organe sensible de la vision, est différente que celle de notre perception, en révélant ce miroir déformant de notre vision, nous n'avons pas provoqué une crise dans notre compréhension de la vision mais nous avons au contraire progressé dans la connaissance de ce système complexe. Notamment, nous avons mis en évidence que cette rétinotopie fovéée n'est efficace qu'avec la capacité de pouvoir explorer notre monde visuel avec notre regard. Que de nouvelles découvertes à venir sur l'intelligence de la vision et du regard !

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

