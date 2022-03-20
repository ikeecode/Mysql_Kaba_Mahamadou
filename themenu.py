class menu:
    menus = [
            "Lister tous les agences",
            "Lister tous les caissiers par ordre croissant de leur nom",
            "Lister tous chef d’agence ainsi que l'adresse de l’agence",
            "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde", #ou une agence qui existe dans la base a defaut de Plateau
            "Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est dunbar par ordre croissant du montant",
            "Lister les utilisateurs de l’agence Plateau",
            "Lister le nombre de compte par agence",
            "Lister les comptes affectés à l’utilisateur dunbar durant le mois de Mai 2021",
            # "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
            # "Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001",
            # "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021\npar ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
            # "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est dunbar par ordre croissant du montant",
            # "Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est dunbar .",
            # "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
            # "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
            # "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
            # "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
            # "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 2021",
            # "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
            # "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 2021",
            # "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 2021",
            # "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 2021",
            # "Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
            # "Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
            # "Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est dunbar"
            ]

    sql_requests = {
            "Lister tous les agences" : 'SELECT * FROM AGENCE',
            "Lister tous les caissiers par ordre croissant de leur nom" : "SELECT u.nom_USER FROM PROFIL p, USERS u WHERE p.libelle_PROFIL = 'caissier'",
            "Lister tous chef d’agence ainsi que l'adresse de l’agence" : "SELECT  nom_USER FROM USERS, AGENCE, PROFIL WHERE libelle_PROFIL like '%chef agence%' AND id_USER = id_USER_USER",
            "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde" : "SELECT DISTINCT numero, solde_COMPTE_TRANSACTION, adresse_AGENCE FROM COMPTE_TRANSACTION, AGENCE, TRANSACTIONS WHERE numero_AGENCE = numero_AGENCE_AGENCE AND adresse_AGENCE like '%American%' ORDER BY solde_COMPTE_TRANSACTION",
            "Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant" : """SELECT SUM(montant_TRANSACTION) AS SOMME, id_USER, nom_USER FROM USERS, TRANSACTIONS, PROFIL, AGENCE WHERE TRANSACTIONS.id_USER_USER = USERS.id_USER AND PROFIL.libelle_PROFIL
                                                                                                                                                                            LIKE '%caissier%' AND AGENCE.numero_AGENCE = ( SELECT numero FROM COMPTE_TRANSACTION, TRANSACTIONS, USERS, AGENCE
                                                                                                                                                                            WHERE COMPTE_TRANSACTION.numero = TRANSACTIONS.numero_COMPTE_TRANSACTION AND TRANSACTIONS.id_USER_USER  = USERS.id_USER AND TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE
                                                                                                                                                                            AND USERS.nom_USER LIKE '%moussa%' ) GROUP BY TRANSACTIONS.id_USER_USER ORDER BY SOMME""",
            "Lister les utilisateurs de l’agence Plateau" : "SELECT nom_USER FROM USERS, PROFIL, AGENCE  WHERE  id_PROFIL_PROFIL = id_PROFIL AND  libelle_PROFIL LIKE '%UTILISATEUR%' AND numero_AGENCE_AGENCE  = numero_AGENCE and adresse_AGENCE LIKE '%PLATEAU%'",
            "Lister le nombre de compte par agence" : "SELECT COUNT(*), adresse_AGENCE  FROM USERS, AGENCE WHERE numero_AGENCE = numero_AGENCE_AGENCE  GROUP BY numero_AGENCE_AGENCE ",
            "Lister les comptes affectés à l’utilisateur dunbar durant le mois de Mai 2021" : "",


            } #ce dico va recevoir les elements de menus comme clés et les valeurs seront les requetes sql correspondantes
