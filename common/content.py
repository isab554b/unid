##############################
#   TABLE OF CONTENTS (A-Z)
#   - Globals
#   - Frontpage / index
#   - About us
#   - Contact
#   - Error
#   - Portfolio
#   - Profile
#   - Services and prices
#   - Signup
#   - Blog


##############################
#   GLOBALS
global_content = {
    # LOGOS
    "logos": {
        "unid": {
            "primary_logo": "primary_logo.svg",
            "logo_alt": "UNID Studio's logo",
        },
    },
    # ICONS
    "ui_icons": {
        "arrow": "arrow.svg",
        "admin": "admin.svg",
        "burger": "burger.svg",
        "card": "card.svg",
        "cart": "cart.svg",
        "checkmark": "checkmark.svg",
        "checkmark_full": "checkmark_full.svg",
        "discount": "discount.svg",
        "discount_full": "discount_full.svg",
        "documents": "documents.svg",
        "education": "education.svg",
        "email": "email.svg",
        "error": "exclamation_mark.svg",
        "eye_closed": "eye_closed.svg",
        "eye_open": "eye_open.svg",
        "folder_closed": "folder_closed.svg",
        "folder_open": "folder_open.svg",
        "hourglass": "hourglass.svg",
        "info": "info.svg",
        "lock": "lock.svg",
        "pen_line": "pen_line.svg",
        "pen":"pen.svg",
        "phone": "phone.svg",
        "message": "letter.svg",
        "stop_watch": "stop_watch.svg",
        "trashcan": "trashcan.svg",
        "user": "user.svg",
        "user_circle": "user_circle.svg",
        "user_name_full": "user_name_full.svg",
        "user_name_semi": "user_name_semi.svg",
        "www": "www.svg",
    },
    # SOME
    "social_media": {
        # Unid
        "unid": {
            "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
            "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
        },
        # Empoyees
        "employees": {
            "denise": {
                "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
                "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
            },
            "isabella": {
                "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
                "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
            },
        },
    },
    # HEADER
    "header": {
        "nav_bar": {
            "nav_items": [
                {"text": "Services & Priser", "link": "/services_and_prices"},
                {"text": "Cases", "link": "/cases"},
                {"text": "Om UNID Studio", "link": "/om_unid_studio"},
                {"text": "Kontakt", "link": "/contact"},
                {"text": "Blog", "link": "/blog"},
            ],
        },
        "header_bar": {
            "selling_points": [
                {"icon": "heart.svg", "text": "Tilfredshedsgaranti"},
                {"icon": "discount.svg", "text": "Studierabat"},
                {"icon": "pen.svg", "text": "Skræddersyet løsning"},
                {"icon": "chat.svg", "text": "Hurtig kundeservice"}
            ],
        },
    },
    # FOOTER
    "footer": {
        "footer_info": [
            "UNID Studio © 2023 • All rights reserved  • CVR nr. 43924451",
            
        ],
    },
    # FORMS
    "form_inputs": {
        # Username
        "username": {
            "label_for": "username",
            "text": "Brugernavn",
            "type": "text",
            "name": "username",
            "inputmode": "text",
            "placeholder": "Loremipsum",
            "form_info": "",
        },
        # Password
        "password": {
            "label_for": "pwd",
            "text": "Adgangskode",
            "type": "password",
            "name": "pwd",
            "inputmode": "text",
            "placeholder": "••••••••",
            "form_info": "Use at least 8 characters, one uppercase, one lowercase and one number.",
        },
        # First name
        "first_name": {
            "label_for": "first_name",
            "text": "Fornavn",
            "type": "text",
            "name": "first_name",
            "inputmode": "text",
            "placeholder": "Lorem",
            "form_info": "",
        },
        # Last name
        "last_name": {
            "label_for": "last_name",
            "text": "Efternavn",
            "type": "text",
            "name": "last_name",
            "inputmode": "text",
            "placeholder": "Ipsum",
            "form_info": "",
        },
        # Email
        "email": {
            "label_for": "email",
            "text": "Email",
            "type": "email",
            "name": "email",
            "inputmode": "email",
            "placeholder": "loremipsum@mail.com",
            "form_info": "",
        },
        # Phone
        "phone": {
            "label_for": "phone",
            "text": "Telefon nummer",
            "type": "tel",
            "name": "phone",
            "inputmode": "tel",
            "placeholder": "12 34 56 78",
            "form_info": "",
        },
        # Website name
        "website_name": {
            "label_for": "website_name",
            "text": "Navn på din hjemmeside",
            "type": "text",
            "name": "website_name",
            "inputmode": "text",
            "placeholder": "Lorem-ipsum.dk",
            "form_info": "",
        },
        # Website url
        "website_url": {
            "label_for": "website_url",
            "text": "URL til din hjemmeside",
            "type": "url",
            "name": "website_url",
            "inputmode": "url",
            "placeholder": "https://www.lorem-ipsum.dk",
            "form_info": "",
        },
        # Full name
        "full_name": {
            "label_for": "name",
            "text": "Navn",
            "type": "name",
            "name": "name",
            "inputmode": "text",
            "placeholder": "Lorem Ipsum",
            "form_info": "",
        },
    },
    #  EMPTY PAGE
    "empty_page": {
        "header_text": "Hov, der er ikke noget her endnu...",
        "subheader_text": "Vi arbejder på noget spændende, så kom tilbage senere!",
    },
}


##############################
#   FRONTPAGE / INDEX
frontpage_content = {
    # HERO SECTION
    "hero_section": {
        "header_text": "Unikke & skræddersyede løsninger",
        "subheader_text": "Vi bestræber os på, at lave unikke og kvalitets løsninger som opfylder hver enkel kundes behov.",
        "button_text": "Kontakt os",
        "image": "frontpage_graphic.png",
    },
    # TESTIMONIAL SECTION
    "testimonials_section": {
        "header_text": "Det siger vores kunder",
        "decorative_header_text": "Anmeldelser",
        "subheader_text": "Er du nysgerrig på, hvad vores kunder har oplevet? Dyk ned i vores anmeldelser og få et ægte indblik i, hvordan vores services har gjort en forskel.",
        "testimonial_icon": "quote.svg",
        # Testiomonials
        "testimonials": [
            {
                "text": "Vi har haft en rigtig god oplevelse med at få lavet vores hjemmeside, www.dragørelservice.dk. UNID Studio har ydet en fantastisk service, været meget hjælpsomme og lyttede virkelig til vores ønsker. De var yderst professionelle og udførte opgaven til perfektion. Vi er meget tilfredse med resultatet!",
                "author_name": "Radwan Radwan",
                "author_job_title": "Dragør El-Service ApS",
            },
            {
                "text": "UNID studio er en lille energisk og grundig virksomhed, der meget konkurrencedygtigt kan hjælpe små og store virksomheder med at udvikle deres digitale tilstedeværelse. De leverer en håndholdt service og er meget imødekommende overfor deres kunders individuelle ønsker og behov.",
                "author_name": "Jens Stanek",
                "author_job_title": "KEA Startup Hub",
            },
        ],
    }
}


##############################
#   ABOUT_US
about_us_content = {
    "header_text": "Om UNID Studio",
    "subheader_text": "Hos UNID Studio er vi et lille, men dynamisk team med store idéer. Vi kombinerer vores omfattende erfaring inden for grafisk design og webudvikling, til at skabe skræddersyede løsninger, der matcher dine unikke behov. ",
    # HIGHLIGHTS SECTION
    "highlights_section": {
        "header_text": "Lille studio - med store idéer",
        "decorative_header_text": "Om UNID Studio",
        # Highlights
        "highlights": [
            {"illustration": "tools.png", "illustration_alt": "Illustration med kreative værktøjer", "title": "Erfaring", "text": "Vi har stor erfaring indenfor grafisk design og udvikling af websites. Med vores ekspertise, kan vi skræddersy en løsning efter dine ønsker og behov."},
            {"illustration": "book.png", "illustration_alt": "Illustration med en bog", "title": "KEA Ignite", "text": "Vi har et samarbejde med KEA. Hvis du er iværksætter, og går på KEA, så giver vi rabat på vores ydelser."},
            {"illustration": "screen.png", "illustration_alt": "Illustration med en skærm med former på", "title": "Tidligere cases", "text": "Vi vægter tilfredshedgaranti højt, og afslutter ikke en case, før kunden er tilfreds. Vores tidligere projekter, kan ses under cases."},
            {"illustration": "phone_mail.png", "illustration_alt": "Illustration med en telefon og et brev", "title": "Kontakt os", "text": "Lad os høre om din idé. Vi er altid parate, til at hjælpe - og vi skræddersyer gerne én løsning til netop din virksomhed."},
        ],
    },
    # VISION SECTION
    "vision_section": {
        "header_text": "Vores vision",
        "decorative_header_text": "Vision",
        "introduction_text": "Vi glæder os over at støtte ambitiøse studerende på deres iværksætterrejse.",
        "illustration": "student_discount.png",
        "illustration_alt": "Grafik til UNID Studio, der tilbyder studierabat på alle deres hjemmesidepakker.",
        # Paragraphs
        "paragraphs": [
            {
                "title": "",
                "text": "Vi tror på, at en stærk start er nøglen til vedvarende vækst – og for at gøre denne start så tilgængelig som muligt, tilbyder vi særlige studierabatter på vores hjemmesidepakker. På den måde ønsker vi at lette byrden for nye forretningsfolk og give dem den nødvendige digitale platform, til at realisere deres visioner.",
            },
            {
                "title": "Hvordan opnår du studierabat?",
                "text": "Jonglerer du med både iværksætteri og uddannelse, så tilbyder vi særlige studierabatter på vores hjemmesidepakker. Det eneste krav vi har til dig, er at du skal være iværksætter samt være indskrevet på en uddannelsesinstitution – og kunne fremvise et gyldigt studiekort. Opnå din studierabat i dag, og lad os sammen bygge fundamentet for din fremtidige succes.",
            },
        ],
    },
    # SKILLS SECTION
    "skills_section": {
        "header_text": "Et udpluk af vores kompetencer",
        "decorative_header_text": "Kompetencer",
        # Skills
        "skills": [
            {"icon": "code.svg", "title": "Kodning"},
            {"icon": "pen.svg", "title": "UI/UX design"},
            {"icon": "documents.svg", "title": "Prototyping"},
            {"icon": "eye_open.svg", "title": "SEO"},
            {"icon": "megaphone.svg", "title": "Digital marketing"},
            {"icon": "desktop.svg", "title": "WordPress"},
 
        ],
    },
    # TEAM SECTION
    "team_section": {
        "header_text": "Bag om teamet - hvem er vi?",
        "decorative_header_text": "Team",
        "introduction_text": "Vi er et dedikeret og kreativt team, som har sans for selv de mindste detaljer. For os er det vigtigt at levere den bedste og mest konkurrencedygtige løsning.",
        # Paragraphs
        "paragraphs": [
            {
                "title": "",
                "text": "Vi, Denise & Isabella, står bag UNID Studio. Vi har begge et stort flair, for at designe og udvikle digitale løsninger. Vi har udarbejdet og leveret mange digitale løsninger, og sammen udgør vi et team, hvor vores forskellige færdigheder og kompetencer komplementerer hinanden godt – og danner grobund for kreative løsninger, der skiller sig ud. Når vi udvikler websites og andre løsninger, vægter vi dine ønsker og behov højt, og på baggrund af det, kommer vi med vores forslag på, hvordan vi sammen kan komme i mål – og få udviklet den bedste løsning til lige netop dig.",
            },
        ],
        # Employees
        "employees": [
            {"employee_image": "denise.jpg", "image_alt": "Portræt af Denise", "employee_name": "Denise Dalvang Hansen", "employee_job_title": "Designer & grafiker", "employee_information": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor, fuga?"},
            {"employee_image": "isabella.jpg", "image_alt": "Portræt af Isabella", "employee_name": "Isabella Hilarius Nielsen", "employee_job_title": "Webudvikler", "employee_information": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor, fuga?"},
        ],
    },
}


##############################
#   CONTACT
contact_content = {
    "header_text": "Kontakt",
    "subheader_text": "Uanset om du har et eller flere spørgsmål, så er vi altid parate, til at hjælpe dig. Lad os høre om din idé, og vi vil herefter i fælleskab skræddersy én løsning, der passer perfekt til dig og din virksomhed. Vi ser frem, til at høre fra dig!",
    "illustration": "contact.png",
    "illustration_alt": "Illustration af grafisk design",
    # CONTACT FORM SECTION
    "contact_form_section": {
        "header_text": "Skriv til os her",
        "subheader_text": "Vi stræber efter at vende tilbage hurtigst muligt.",
        "button_text": "Send besked",
    }
}


##############################
#   ERROR
error_content = {
    "header_text": "Hov! Der skete en fejl",
    "illustration": "unid_universe.svg",
    "illustration_alt": "Illustration af UNID Universe",
    "button_link": "/",
    "button_text": "Gå til forsiden",
    "404": {
        "error_title_text": "Fejl 404: Siden blev ikke fundet",
        "error_message_text": "Beklager, men den side, du forsøgte at tilgå, eksisterer ikke. Tjek venligst URL'en og prøv igen, eller kontakt os, hvis problemet fortsætter."
    },
    "500": {
        "error_title_text": "Fejl 500: Intern Serverfejl",
        "error_message_text": "Vi beklager, men der er sket en fejl på serveren, som forhindrer udførelsen af din anmodning. Prøv venligst igen senere, eller kontakt os, hvis problemet fortsætter."
    },
}


##############################
#   LOGIN
login_content = {
    "header_text": "Log ind",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "button_text": "Log ind",
    "illustration": "unid_universe.svg",
    "illustration_alt": "Illustration af UNID Universe",
}


##############################
#   PORTFOLIO
portfolio_content = {
    "header_text": "Cases",
    "subheader_text": "Velkommen til vores cases! Her kan du se vores seneste arbejde og projekter, hvor vi har skabt unikke visuelle identiteter, logoer, websites og meget mere.",
    "cases_section": [
        {"icon": "user.svg", "text": "Oversigt", "template": "profile_overview"},
        {"icon": "card.svg", "text": "Klippekort", "template": "profile_admin_clipcard"},
        {"icon": "stop_watch.svg", "text": "Timeregistrering", "template": "profile_admin_hour_registration"},
        {"icon": "letter.svg", "text": "Beskeder", "template": "profile_admin_messages"},
        {"icon": "settings.svg", "text": "Indstillinger", "template": "profile_settings"},
    ],
    # Cases
    "cases": [
            {"illustration": "imput1.webp", "illustration_alt": "Billede af Imputs forside", "title": "Imput", "link": "/imput"},
            {"illustration": "nomi1.jpg", "illustration_alt": "Billede af Nomi Creations forside", "title": "Nomi Creations", "link": "/nomi_creations"},
            {"illustration": "dragoer3.webp", "illustration_alt": "Billede af Dragør El-Services forside", "title": "Dragør El-Service", "link": "/dragoer_el_service"},
        ],
}


##############################
#   PROFILE
profile_content = {
    # GLOBAL
    "logout": {
        "header_text": "Log ud",
        "subheader_text": "Du er ved at logge ud, er du sikker?",
        "button_texts": {
            "cancel": "Annuller",
            "proceed": "Log ud"
        }
    },
    # ADMIN SPECIFIC
    "admin_specific_content": {
        "profile_admin_clipcard": {
            "header_text": "Aktive klippekort",
            "decorative_header_text": "Klippekort",
        },
        "profile_admin_hour_registration": {
            "header_text": "Timeregistrering",
            "decorative_header_text": "Registrering",
        },
        "profile_admin_messages": {
            "header_text": "Indsendte beskeder",
            "decorative_header_text": "Beskeder",
        },
        "profile_admin_settings": {
            "header_text": "Aktive brugere",
            "decorative_header_text": "Indstillinger",
        },
        "profile_admin_subscriptions": {
            "header_text": "Aktive abonnementer",
            "decorative_header_text": "Abonnementer",
        },
        # Menu
        "admin_profile_menu": [
            {"icon": "user.svg", "text": "Oversigt", "template": "profile_overview"},
            {"icon": "card.svg", "text": "Klippekort", "template": "profile_admin_clipcard"},
            {"icon": "stop_watch.svg", "text": "Timeregistrering", "template": "profile_admin_hour_registration"},
            {"icon": "cart.svg", "text": "Abonnementer", "template": "profile_admin_subscriptions"},
            {"icon": "letter.svg", "text": "Beskeder", "template": "profile_admin_messages"},
            {"icon": "settings.svg", "text": "Indstillinger", "template": "profile_admin_settings"},
        ],
    },
    # CUSTOMER SPECIFIC
    "customer_specific_content": {
        "profile_customer_subscription": {
            "header_text": "Køb et abonnement",
            "decorative_header_text": "Abonnement",
        },
        "profile_customer_clipcard": {
            "header_text": "Det, har du fået lavet",
            "decorative_header_text": "Timeregistrering",
        },
        "profile_customer_messages": {
            "header_text": "Skriv til os her",
            "decorative_header_text": "Beskeder",
            "box_header_text": "Send en besked",
        },

        "profile_customer_settings": {
            "header_text": "Brugerindstillinger",
            "decorative_header_text": "Indstillinger",
        },
        # Menu
        "customer_profile_menu": [
            {"icon": "user.svg", "text": "Oversigt", "template": "profile_overview"},
            {"icon": "card.svg", "text": "Klippekort", "template": "profile_customer_clipcard"},
            {"icon": "cart.svg", "text": "Abonnement", "template": "profile_customer_subscription"},
            {"icon": "letter.svg", "text": "Beskeder", "template": "profile_customer_messages"},
            {"icon": "settings.svg", "text": "Indstillinger", "template": "profile_customer_settings"},
        ],
    },
    # BUY CLIPCARD
    "buy_clipcard": {
        "header_text": "Køb af klippekort",
        "decorative_header_text": "Klippekort",
    },
    # CONFIRMATION
    "confirmation": {
        "header_text": "Betalingsbekræftelse",
        "decorative_header_text": "Bekræftelse",
    }
}


##############################
#   SERVICES_AND_PRICES
services_and_prices_content = {
    "header_text": "Services og priser",
    "subheader_text": "Vi tilbyder en bred vifte af professionelle løsninger, der er skræddersyet til dine behov. Hos os finder du en gennemsigtig prissætning, så du altid ved, hvad du får for pengene. Kontakt os i dag for at få et uforpligtende tilbud.",
    # SERVICES SECTION
    "services_section": {
        "header_text": "Det kan vi hjælpe dig med",
        "decorative_header_text": "Services",
        "illustration": "services.png",
        "illustration_alt": "Grafik der illustrerer de services UNID Studio tilbyder.",
        # Paragraphs
        "paragraphs": [
            {
                "title": "Websites",
                "text": "Vi bruger WordPress, til at udvikle websites. Hvis du har specifikke ønsker, kan vi i det fleste tilfælde efterleve disse, da vi kan foretage ændringer direkte i koden – og udvikle sitet efter dit ønske og tilpasse det dine behov.",
            },
            {
                "title": "Design af prototyper",
                "text": "Skal du udvikle en app og mangler et design? Eller har du brug for en prototype til dit website? Vi designer professionelle interaktive prototyper i Figma, som kan bruges til brugertests, eller til at sende direkte til din udvikler.",
            },
            {
                "title": "Visuel identitet & grafisk design",
                "text": "Mangler du en visuel identitet, vil være letgenkendelig og skille dig ud fra mængden? Så kan vi hjælpe dig med at skabe en unik identitet. På baggrund af dine ønsker, kan vi udforme et logo, en farvepalette og finde typografier. Vi har også ekspertise indenfor grafisk design, og kan hjælpe med grafisk opsætning af layout, visitkort, brochurer, plakater samt udarbejdelse af SoMe content.",
            },
            {
                "title": "Vedligeholdelse",
                "text": "Vi håndterer gerne vedligeholdelsen af dit website, så det altid er opdateret, sikkert og kører optimalt. Med regelmæssige opdateringer og løbende overvågning sørger vi for, at dit site fungerer fejlfrit.",
            },
        ],
    },
    # SUBSCRIPTION SECTION
    "subscription_section": {
        "header_text": "Lad os håndtere vedligeholdesen",
        "decorative_header_text": "Abonnement",
        "introduction_text": "Er du træt af at bruge tid på vedligeholdelsen af dit website? Lad os tage ansvaret for opdateringer, sikkerhed og drift.",
        # Paragraphs
        "paragraphs": [
            {
                "title": "Websites",
                "text": "Fokuser på din virksomhed, mens vi tager os af vedligeholdelsen af dit website. Med vores ekspertise sikrer vi, at dit site altid er opdateret, sikkert og fungerer optimalt. Lad os håndtere detaljerne, så du kan bruge din tid på det, der virkelig betyder noget.",
            },
        ],
        "subscriptions": {
            # Subscription default
            "subscription_default": {
                "subscription_a": {
                    "button_text": "Køb nu",
                    "info": {
                        "title": "Abonnement",
                        "hours": "Abonnement",
                        "price": "300 DKK pr. måned",
                    },
                    "selling_points": [
                        {"text": "Kontrol af ydeevne og hastighed for hjemmesiden"},
                        {"text": "Regelmæssige opdateringer af både tema og plugins"},
                        {"text": "Overvågning af hjemmesiden med Google Search Console"},
                        {"text": "30 minutters sparring / vores ekspertise til udbedring af fejl"},
                    ]
                },
            },
        }
    },
    # PRICES SECTION
    "prices_section": {
        "header_text": "Find den rette pakke til dig",
        "decorative_header_text": "Priser",
        "paragraph_title": "Vi tilbyder kun det bedste. Skræddersyede, professionelle websites med tilfredshedsgaranti.",
        "paragraph_text": "Med tilfredshedsgaranti på alle vores ydelser afsluttes projektet først, når du har godkendt det. Ved opstart betales 50% af den aftalte pris, derefter påbegyndes arbejdet. Når projektet er godkendt og afsluttet, betales det resterende beløb.",
        "pricings": {
            # Pricing default
            "pricing_default": {
                "price_a": {
                    "info": {
                        "title": "- til den lille start up",
                        "hours": "Get started",
                        "discount": "6.400 DKK",
                        "price": "8.000 DKK",
                    },
                    "selling_points": [
                        {"text": "Opstartsmøde"},
                        {"text": "Installation af WordPress"},
                        {"text": "Opsætning og tilpasning af tema"},
                        {"text": "Implementering af visuel identitet"},
                        {"text": "Opsætning af op til 5 sider"},
                        {"text": "Professionelt design"},
                        {"text": "Kontaktformular"},
                        {"text": "SEO optimering"},
                        {"text": "Mobilvenlig (Responsivt layout)"},
                    ]
                },
                "price_b": {
                    "info": {
                        "title": "– til dig der vil godt i gang",
                        "hours": "Let's go",
                        "discount": "9.600 DKK",
                        "price": "12.000 DKK",
                    },
                    "selling_points": [
                        {"text": "Opstartsmøde"},
                        {"text": "Installation af WordPress"},
                        {"text": "Opsætning og tilpasning af tema"},
                        {"text": "Implementering af visuel identitet"},
                        {"text": "Opsætning af op til 8 sider"},
                        {"text": "Professionelt design"},
                        {"text": "Kontaktformular"},
                        {"text": "SEO optimering"},
                        {"text": "Mobilvenlig (Responsivt layout)"},
                        {"text": "1 times support"},
                    ]
                },
                "price_c": {
                    "info": {
                        "title": "– til dig der vil have en webshop",
                        "hours": "Get paid",
                        "discount": "14.800 DKK",
                        "price": "18.500 DKK",
                    },
                    "selling_points": [
                        {"text": "Opstartsmøde"},
                        {"text": "Installation af WordPress"},
                        {"text": "Opsætning og tilpasning af tema"},
                        {"text": "Implementering af visuel identitet"},
                        {"text": "Opsætning af op til 8 sider"},
                        {"text": "Professionelt design"},
                        {"text": "Kontaktformular"},
                        {"text": "SEO optimering"},
                        {"text": "Mobilvenlig (Responsivt layout)"},
                        {"text": "2 timers support"},
                        {"text": "Webshop"},
                        {"text": "Oprettelse af 10 produkter"},
                    ]
                },
            },
        }
    },
    # ADDON SECTION
    "addon_section": {
        "header_text": "Tilkøb",
        "addons": {
            # Addon default
            "addon_default": {
                "addon_a": {
                    "info": {
                        "title": "Visuel indentitet",
                        "text": "Indeholder logo, farver, typografi, evt. 5. element samt designguide.",
                        "price": "7.000 DKK",
                    },     
                },
                "addon_b": {
                    "info": {
                        "title": "Sider",
                        "text": "Har du brug for flere sider på dit website? Prisen er pr. side.",
                        "price": "650 DKK",
                    },     
                },
                "addon_c": {
                    "info": {
                        "title": "Udvidet SEO",
                        "text": "Bliv fundet i søgemaskinerne med onsite SEO. Prisen er pr. side.",
                        "price": "300 DKK",
                    },   
                },
                "addon_d": {
                    "info": {
                        "title": "Blog",
                        "text": "Blogfunktion og skabelon til blogindlæg.",
                        "price": "950 DKK",
                    },  
                },
                "addon_e": {
                    "info": {
                        "title": "Oprettelse af produkter",
                        "text": "Vi står gerne, for at oprette dine produkter. Prisen er for 10 produkter.",
                        "price": "650 DKK",
                    },  
                },
                "addon_f": {
                    "info": {
                        "title": "Domæne & hosting",
                        "text": "Få os, til at stå for køb og oprettelse af dit domæne og webshoting.",
                        "price": "650 DKK",
                    },  
                },
                "addon_g": {
                    "info": {
                        "title": "Nyhedsbrev eller pop-up",
                        "text": "Nyhedsbrevsfunktion eller en pop-up, som dukker op, når en kunde besøger dit website.",
                        "price": "650 DKK",
                    },  
                },
                "addon_h": {
                    "info": {
                        "title": "Support",
                        "text": "En times support, der giver adgang til vores ekspertise.",
                        "price": "650 DKK",
                    },  
                },
            },
        }
    },
    # CLIPCARD SECTION
    "clipcard_section": {
        "header_text": "Spar din dyrebare tid med et klippekort",
        "decorative_header_text": "Klippekort",
        "clipcards": {
            # Clipcard default
            "clipcard_default": {
                "clipcard_a": {
                    "button_text": "Køb nu",
                    "info": {
                        "title": "Klippekort",
                        "hours": "10 timer",
                        "price": "7.000 DKK",
                    },
                    "selling_points": [
                        {"text": "Adgang til vores ekspertise"},
                        {"text": "Vælg frit hvad timerne bruges på"},
                        {"text": "Nemt anmode om opgaveønsker"},
                        {"text": "Overblik over udførte opgaver"},
                        {"text": "Overblik over tidsforbrug"},
                        
                    ]
                },
                "clipcard_b": {
                    "button_text": "Køb nu",
                    "info": {
                        "title": "Klippekort",
                        "hours": "20 timer",
                        "price": "14.000 DKK",
                    },
                    "selling_points": [
                        {"text": "Adgang til vores ekspertise"},
                        {"text": "Vælg frit hvad timerne bruges på"},
                        {"text": "Nemt anmode om opgaveønsker"},
                        {"text": "Overblik over udførte opgaver"},
                        {"text": "Overblik over tidsforbrug"},
                    ]
                },
                "clipcard_c": {
                    "button_text": "Køb nu",
                    "info": {
                        "title": "Klippekort",
                        "hours": "30 timer",
                        "price": "19.500 DKK",
                    },
                    "selling_points": [
                        {"text": "Adgang til vores ekspertise"},
                        {"text": "Vælg frit hvad timerne bruges på"},
                        {"text": "Nemt anmode om opgaveønsker"},
                        {"text": "Overblik over udførte opgaver"},
                        {"text": "Overblik over tidsforbrug"},
                    ]
                },
            },
        }
    },

}


##############################
#   SIGNUP
signup_content = {
    "header_text": "Opret bruger",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "button_text": "Opret bruger",
}

##############################
#   BLOG
blog_content = {
    "header_text": "Blog",
    "subheader_text": "Velkommen til vores blog! Her deler vi vores indsigt, erfaringer og de seneste trends inden for design og udvikling. Vi tilbyder inspiration og praktiske tips, der hjælper dig med at forstå og navigere i den digitale verden.",
    "posts": {
            # Clipcard default
            "post_default": {
                "post_d": {
                    "info": {
                        "title": "WordPress webshop i WooCommerce - Er det gratis at lave en webshop?",
                        "description": "At oprette en webshop kan være en spændende rejse, men det kræver også en vis tålmodighed og forståelse af platformen. En populær løsning til at bygge en webshop er WordPress i kombination med WooCommerce...",
                        "author": "Denise Hansen",
                        "date": "30. september 2024",
                        "link": "/wordpress-webshop-i-woocommerce",
                        "image": "webshop.webp",
                        "image_alt": "Grafik til webshop udviklet i WordPress med WooCommerce.",

                    },
                },
                "post_c": {
                    "info": {
                        "title": "Hvem laver gode hjemmesider? - Kvalitet versus pris",
                        "description": "Når du står overfor at skulle vælge en webdesigner eller webudvikler til din hjemmeside, kan det være fristende at vælge det billigste tilbud. Men ofte er det ikke prisen, der er den vigtigste indikator for kvalitet...",
                        "author": "Denise Hansen",
                        "date": "29. september 2024",
                        "link": "/hvem-laver-gode-hjemmesider",
                        "image": "hjemmeside.webp",
                        "image_alt": "Grafik til hvem der laver gode hjemmesider.",

                    },
                },
                "post_b": {
                    "info": {
                        "title": "Hastighedsoptimer din WordPress-hjemmeside",
                        "description": "Er du træt af, at din WordPress-hjemmeside loader langsomt? En langsom hjemmeside kan koste dig dyrebare besøgende og skade din søgemaskinerangering. Heldigvis er der en række ting, du kan gøre for at optimere din hjemmesides hastighed...",
                        "author": "Denise Hansen",
                        "date": "5. september 2024",
                        "link": "/hastighedsoptimer-din-wordpress-hjemmeside",
                        "image": "wp_hastighedsoptimering.webp",
                        "image_alt": "Grafik af hastighedsoptimering på WordPress side.",

                    },
                },
                "post_a": {
                    "info": {
                        "title": "Hastighedsoptimering på hjemmesider er en nødvendighed!",
                        "description": "Hastighedsoptimering er en vigtig faktor, der påvirker brugeroplevelsen, SEO, konverteringsrater og dit brand som helhed. En hurtig hjemmeside holder brugerne engagerede, forbedrer søgemaskine rangeringer...",
                        "author": "Denise Hansen",
                        "date": "5. september 2024",
                        "link": "/hastighedsoptimering-paa-hjemmesider-er-en-noedvendighed",
                        "image": "hastighedsoptimering.webp",
                        "image_alt": "Grafik af hastighedsoptimering på hjemmeside.",

                    },
                },               
            },
        }
} 