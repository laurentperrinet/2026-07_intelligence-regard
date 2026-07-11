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
  <meta name="dc.modified" content="2026-07-11T10:06:44+00:00" />
  <meta property="article:modified_time" content="2026-07-11T10:06:44+00:00" />
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
  <link rel="alternate" type="text/html" href="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e55dd9f9a0c583770be76e5b416cd61b3628d278/" />
  <meta name="manubot_html_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e55dd9f9a0c583770be76e5b416cd61b3628d278/" />
  <meta name="manubot_pdf_url_versioned" content="https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e55dd9f9a0c583770be76e5b416cd61b3628d278/manuscript.pdf" />
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
([permalink](https://laurentperrinet.github.io/2026-07_intelligence-regard/v/e55dd9f9a0c583770be76e5b416cd61b3628d278/))
was automatically generated
from [laurentperrinet/2026-07_intelligence-regard@e55dd9f](https://github.com/laurentperrinet/2026-07_intelligence-regard/tree/e55dd9f9a0c583770be76e5b416cd61b3628d278)
on July 11, 2026.
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




Et si l’on vous révélait que le monde visuel que vous percevez en ce moment même est une reconstruction déformée de la réalité ? Pur non-sens ! Intuitivement, nous pensons que notre perception de l’environnement lumineux qui nous entoure est fidèlement calquée sur nos sensations. Pourtant, l’image qui se forme sur la rétine, l’organe sensible de la vision, présente une géométrie précisément déformée. Étudier cette propriété fondamentale de la vision est essentiel : cela permet de mieux la comprendre, de développer des moyens de soigner les pathologies visuelles, ou encore d’exploiter ces principes biologiques pour concevoir des systèmes d’intelligence artificielle plus robustes et moins énergivores, en clair, à faire « sens de nos sens ». Je suis chercheur en neurosciences computationnelles, et m’attache à décrypter la manière dont le cerveau assemble les fragments d’information pour effectuer des « calculs » — comme, par exemple, la capacité à percevoir ce texte que vous lisez. Je vais vous exposer ici les découvertes récentes sur la façon dont la géométrie de la rétine façonne notre perception visuelle.


# La rétine, organe sensible de la vision

La vision, quel miracle ! La perception visuelle semble pourtant si simple : il suffit d’ouvrir les yeux, alors que les mécanismes sous-jacents sont d’une complexité impressionnante. Chez l’humain, c’est une fine pellicule de cellules tapissant le fond de l’œil qui fait office de capteur : la rétine. Elle reçoit la lumière concentrée par l’optique oculaire et la transforme en un signal électrochimique ; le flux de photons y est converti en quelques millisecondes par des neurones en une information que le cerveau peut interpréter. Une découverte majeure a révélé que de nombreuses aires cérébrales conservent cette organisation topographique dite rétinotopique : les neurones situés à proximité les uns des autres dans une même aire correspondent à des points proches dans le champ visuel.

## La rétine, un miroir déformant
Notre expérience révèle que notre regard est mobile dans la scène visuelle. Le point de fixation de l’œil, ce point précis de l’espace visuel que vous fixez en ce moment même sur ces mots, se déplace continuement, par exemple vers le prochain mot. Hors, la rétinotopie humaine présente la particularité d’accorder une importance disproportionnée à la région, appelée la fovéa, entourant ce point de fixation. Pour se donner une idée quantitative, la macula, qui entoure la fovéa, correspond dans l’espace visuel à un disque d’environ 5 degrés d’angle visuel — soit la taille de votre paume à bout de bras. Si l’on compare ces 5 degrés aux 180 degrés d’angle visuel en azimut et aux 120 degrés en élévation, on réalise qu’elle n’occupe que 3 millièmes de la surface totale. Pourtant, la rétinotopie humaine est telle qu’environ un quart des fibres du nerf optique proviennent de ce minuscule disque. Cette disproportion est cruciale pour comprendre la vision : les photorécepteurs de la macula sont principalement des cônes, sensibles à la couleur, tandis que le reste de la rétine est majoritairement composé de bâtonnets, sensibles aux faibles intensités lumineuses. Ceci révèle un paradoxe : la grande majorité de notre champ visuel est très largement aveugle aux couleurs, et pourtant notre perception des couleurs semble uniforme, notamment en périphérie.

## Et la rétine chez d'autres espèces?
Cette organisation rétinotopique fovéée est présente chez de nombreuses espèces animales, notamment chez les mammifères. Toutefois, on observe une grande diversité entre les espèces. Chez le chat, par exemple, la densité des photorécepteurs est ainsi plus allongée sur l’axe horizontal, alors qu’elle est quasi uniforme chez le lapin ou la souris. Chaque espèce perçoit donc le monde de manière adaptée à sa niche écologique. Par exemple, certaines espèces comme les faucons ou certains dauphins possèdent même deux paires de fovéas : l’une dédiée à la navigation dans l’axe du mouvement, l’autre à la vision latérale.


# Un enjeu clinique crucial

En quoi est‑il utile d’étudier la géométrie de la rétine ? Tout d’abord car cet aspect de la vision humaine est essentiel pour comprendre les nombreuses pathologies qui peuvent affecter notre vision. L’une de ces pathologies est la dégénérescence maculaire liée à l’âge (DMLA), qui touche surtout la macula que nous avons décrite ci‑dessus. Avec le vieillissement de la population, la DMLA est devenue la première cause de malvoyance chez les personnes de plus de 50 ans. Avec l’importance de la macula que nous soulignée, on comprend mieux pourquoi l’effet de cette maladie est particulièrement délétère : elle invisibilise tout objet placé au centre de notre regard (par exemple visages ou lettres), perturbant ainsi fortement et durablement la vie quotidienne.  Avec le Dr Kevin Mairot de l’AP‑HM, nous utilisons des outils d’intelligence artificielle pour détecter des formes rares de DMLA, avec une efficacité souvent supérieure à celle des spécialistes. L’objectif n’est bien sûr pas de remplacer le practicien, mais plutôt de l’aider dans son diagnostic en complément de l'ensemble des connaissances sur le patient.

Un riche inventaire d’autres pathologies visuelles existe : elles sont diverses et souvent méconnues, ce qui peut provoquer une errance médicale et retarder leur prise en charge. Par exemple, une forme de la maladie d’Alzheimer peut impacter spécifiquement les voies visuelles, depuis la rétine jusqu’au cortex occipito‑pariétal qui concentre les aires visuelle primaires et qui est essentiel à la perception visuelle. Une conséquence peut alors être une altération de la reconnaissance des visages et de leurs émotions, ce qui nuit gravement à la vie sociale. Une forme de cette pathologie affecte notamment le champ périphérique ; notre vision du monde se rétrécit alors autour du centre de notre regard, créant ce que l’on appelle un « effet tunnel ». Le docteur Lejla Koric, à l’AP‑HM, conduit des études novatrices pour diagnostiquer, à partir de réponses comportementales visuelles, de façon précoce ces formes de la maladie d’Alzheimer, afin de les traiter mieux et plus tôt.

Ainsi, les pathologies rétiniennes n'affectent pas seulement la perception visuelle mais peuvent aussi avoir des conséquences délétères sur notre contrôle du mouvement des yeux. En effet nous avons vu que la rétinotopie humaine concentre de grandes resources à la macula qui se concentre autour du point de fixation, lui-même controlé par nos mouvements du regard. La dégénérescence de cette zone du champ visuel peut fortement perturber le contrôle de ce mouvement, générant par exemple des saccades involontaires ou contrôle ineficcace du suivi d'objets en mouvement. Ceci peut induire une difficulté à lire ou à reconnaitre des visages, avec des impacts personnels délétères. Des solutions thérapeutiques innovantes sont proposées, par exemple en utilisant des casques de réalité virtuelle couplés avec des détecteurs de la position du regard qui permettent de faciliter une rééducation du contrôle du regard. [Castet & Calabrese]

# L'outil de la modélisation

Afin de mieux comprendre le rôle de la rétinotopie dans la vision, un outil essentiel est la modélisation. C'est en construisant de toute pièce un système visuel reproduisant efficacément les caractéristiques humaines que l'on peut alors manipuler certaines pièces de cet assemblage et comprendre leur rôle causal dans la mécanique globale. C'est ce que nous avons fait en utilisant un modèle existant appelé convNext, qui est ce qui se fait de mieux actuellement en vision par ordinateur et intelligence artificielle pour identifier des classes (par exemple "labrador" ou "clavier") dans des images arbitraires. Nous avons testé les capacités de ce réseau en lui présentant soit les images classiques, soit des images transformées par la rétinotopie humaine. De façon surprenante, le réseau reste efficace avec les images déformées et mieux, il démontre de nouvelles capacités, comme celle de découvrir un animal camouflé dans une scène visuelle.

Cette nouvelle capacité de notre modèle à localiser des objets visuels constitue une porte ouverte à de nouveaux progrès aussi bien en IA qu'en neurosciences. En effet, le nombre de capteurs visuels et caméras, depuis chaque téléphone intelligent aux voitures connectées, suit une croissance exponentielle, et chacun de ces capteurs requiert des traitement de plus en plus complexes.. Ceci démultiplie les couts énergétiques, ce qui rend critique le besoin de gérer ces contraintes. En utilisant en priorité les pixels autour d'une région d'intéret, on peut ainsi diviser les coûts de traitements d'un facteur significatif. De plus ces systèmes peuvent permettre de répondre plus rapidement ce qui est crucial par exemple dans la nouvelle génération de voitures.

De façon complémentaire, cette voie de recherche soulève un nouvel axe de recherche en neurosciences de la vision. En effet notre perception de la scène visuelle semble uniforme et pourtant nous avons mis en évidence qu'elle est concentrée autour du point de fixation de notre regard. De façon mécanique, nos sensations en périphérie sont fortement dégradées, floue et sans couleur. Comment alors détecter qu'il y aurait un nouveau point d'intéret dans cette zone, c'est-à-dire que plutôt que d'exploiter l'expace visuel sous notre regard, il y a un intéret à déplacer notre regard pour une nouvelle exploration de l'espace visuel? Cette question révèle le lien intime entre la sensation produite par la rétine et l'ensemble du système qui nous permet de déplacer notre regard. Ce point nous encourage à une nouvelle approche pour construire ce type de modèles en leur donnant la liberté d'agir sur le monde environnant, une capacité largement sous exploitée dans les systèmes actuels d'intelligence artificielle.

# Conclusion

Pour conclure, en mettant en lumière que la géométrie de l'oeil, l'organe sensible de la vision, est différente que celle de notre perception, en révélant ce miroir déformant de notre vision, nous n'avons pas provoqué une crise dans notre compréhension de la vision mais nous avons au contraire progressé dans la connaissance de ce système complexe. Notamment, nous avons mis en évidence que cette rétinotopie fovéée n'est efficace qu'avec la capacité de pouvoir explorer notre monde visuel avec notre regard. Il reste par conséquent encore de nombreux aspects à découvrir sur l'intelligence intime entre vision et regard.

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

