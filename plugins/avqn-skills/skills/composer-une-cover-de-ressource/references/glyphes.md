# La banque de glyphes (24 objets)

SVG en viewBox 0 0 24 24, fill none, stroke-linecap/linejoin round. Squelette :

    <svg viewBox="0 0 24 24" width="LARGEUR" height="LARGEUR" fill="none" stroke="TRAIT"
         stroke-width="SW" stroke-linecap="round" stroke-linejoin="round">…</svg>

- TRAIT : #FBF8F1 (ou rgba(251,248,241,.85-.9)) sur rampe sombre ; #16233F sur rampe claire.
- ACCENT (un seul par glyphe) : #F5B326 sur sombre, #E8763A sur clair. Remplacer ACCENT dans les codes ci-dessous.
- SW = 8 × 24 ÷ LARGEUR (trait visuel ≈ 8 px au master). Héros 200-290 px → SW 0.65-0.95 ; satellite 110-135 px → SW 1.4-1.75.
- Étendre la banque : formes simples uniquement (rect, circle, path courts), objet reconnaissable du quotidien, un accent max.

## horloge

    <circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2" stroke="ACCENT"></path>

## prise

    <path d="M9 3.5v3.5M15 3.5v3.5" stroke="ACCENT"></path><path d="M7 7h10v3.5a5 5 0 01-5 5 5 5 0 01-5-5z"></path><path d="M12 15.5v5"></path>

## jauge

    <rect x="2.5" y="9" width="19" height="6.5" rx="3.25"></rect><rect x="4.8" y="11.2" width="10.5" height="2.1" rx="1" fill="ACCENT" stroke="none"></rect>

## enveloppe

    <rect x="2.5" y="5" width="19" height="14" rx="2"></rect><path d="M3.5 7l8.5 5.5L20.5 7"></path>

## checklist

    <rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M8 7.5h8M8 11h8"></path><path d="M8 15.5l2 2 4-4" stroke="ACCENT"></path>

## calendrier

    <rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 9.5h18M8.5 3v4M15.5 3v4"></path><circle cx="12" cy="15" r="1.8" fill="ACCENT" stroke="none"></circle>

## engrenage

    <circle cx="12" cy="12" r="4"></circle><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M18.7 5.3l-2.1 2.1M7.4 16.6l-2.1 2.1"></path>

## manuel

    <path d="M12 6C9.8 4.4 7 4 3.5 4v15c3.5 0 6.3.4 8.5 2 2.2-1.6 5-2 8.5-2V4C17 4 14.2 4.4 12 6z"></path><path d="M12 6v15"></path>

## bulle

    <path d="M4 6a2 2 0 012-2h12a2 2 0 012 2v8a2 2 0 01-2 2H10l-4 4v-4H6a2 2 0 01-2-2z"></path><circle cx="9" cy="10" r="1" fill="ACCENT" stroke="none"></circle><circle cx="12.5" cy="10" r="1" fill="ACCENT" stroke="none"></circle><circle cx="16" cy="10" r="1" fill="ACCENT" stroke="none"></circle>

## eclair

    <path d="M13 2.5L5.5 13.5h5.5L10 21.5l8.5-11H13z" stroke="ACCENT"></path>

## loupe

    <circle cx="10.5" cy="10.5" r="6.5"></circle><path d="M15.3 15.3L21 21"></path>

## cle

    <circle cx="7.5" cy="7.5" r="4.5"></circle><path d="M10.7 10.7L19.5 19.5"></path><path d="M15.8 15.8l2.4-2.4M18.6 18.6l2.4-2.4"></path>

## base-de-donnees

    <ellipse cx="12" cy="5.5" rx="8" ry="3"></ellipse><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13"></path><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3" stroke="ACCENT"></path>

## serveur

    <rect x="3" y="4" width="18" height="7" rx="2"></rect><rect x="3" y="13" width="18" height="7" rx="2"></rect><circle cx="7" cy="7.5" r="1" fill="ACCENT" stroke="none"></circle><circle cx="7" cy="16.5" r="1" fill="ACCENT" stroke="none"></circle>

## cadenas

    <rect x="5" y="10.5" width="14" height="10" rx="2"></rect><path d="M8 10.5V7a4 4 0 018 0v3.5"></path><circle cx="12" cy="15.5" r="1.5" fill="ACCENT" stroke="none"></circle>

## dossier

    <path d="M3 7a2 2 0 012-2h4l2 2.5h9a1.5 1.5 0 011.5 1.5V18a2 2 0 01-2 2H5a2 2 0 01-2-2z"></path>

## sablier

    <path d="M6.5 3h11M6.5 21h11"></path><path d="M8 3v3.2c0 2 1.5 3.6 4 5.8 2.5-2.2 4-3.8 4-5.8V3M8 21v-3.2c0-2 1.5-3.6 4-5.8 2.5 2.2 4 3.8 4 5.8V21"></path><circle cx="12" cy="18" r="1.2" fill="ACCENT" stroke="none"></circle>

## graphique

    <path d="M4 4v16h16"></path><path d="M7 15.5l4-4.5 3 3 5-6.5" stroke="ACCENT"></path>

## fusee

    <path d="M12 2.5c3 2 4.5 5.5 4.5 9.5 0 2-.5 4-1.5 6h-6c-1-2-1.5-4-1.5-6 0-4 1.5-7.5 4.5-9.5z"></path><circle cx="12" cy="10" r="1.9" stroke="ACCENT"></circle><path d="M7.8 14.5L5.5 18.5l3.2-.5M16.2 14.5l2.3 4-3.2-.5"></path>

## cible

    <circle cx="12" cy="12" r="8.5"></circle><circle cx="12" cy="12" r="4.5"></circle><circle cx="12" cy="12" r="1.3" fill="ACCENT" stroke="none"></circle>

## ampoule

    <path d="M12 3a6.2 6.2 0 00-3.6 11.2c.8.6 1.3 1.4 1.5 2.3h4.2c.2-.9.7-1.7 1.5-2.3A6.2 6.2 0 0012 3z"></path><path d="M9.9 19.5h4.2M10.6 21.5h2.8"></path><circle cx="12" cy="9.5" r="1.2" fill="ACCENT" stroke="none"></circle>

## micro

    <rect x="9.5" y="3" width="5" height="10.5" rx="2.5"></rect><path d="M6 11.5a6 6 0 0012 0M12 17.5V21M9 21h6"></path><circle cx="12" cy="8" r="1" fill="ACCENT" stroke="none"></circle>

## soleil

    <circle cx="12" cy="12" r="4.5"></circle><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.2 5.2l2.1 2.1M16.7 16.7l2.1 2.1M18.8 5.2l-2.1 2.1M7.3 16.7l-2.1 2.1"></path>

## lune

    <path d="M19 13.5A7.5 7.5 0 1110.5 5a6 6 0 008.5 8.5z"></path>
