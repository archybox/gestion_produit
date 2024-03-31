import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from json import dump, load
import os


tk_produits=[]
file_path = "file.json"

if os.path.exists(file_path):
    with open(file_path,'r') as file:
        tk_produits=load(file)
        print('-----Gestion-Produits--------')
else:
    print("Fichier n'est pas trouvé.")
    # input('Taper Entrer pour creer un noveau fichier vide. ')
    with open(file_path, 'w') as new_file:
        dump([], new_file)
    with open(file_path,'r') as file:
        tk_produits=load(file)    
    print("Fichier est crée.")
    print('-----Gestion-Produits--------')

# Création de la fenêtre
fenetre_main = tk.Tk()
fenetre_main.title("Gestion de Produits")

# Création d'une étiquette pour afficher le texte
titre_main = tk.Label(fenetre_main, text="Gestion de Produits")
titre_main.pack()


file_label = tk.Label(fenetre_main, text="")
file_label.config(text="Fichier ouvert : " + file_path)
file_label.pack(pady=10)



# Définition de ce qui se passe lorsque le bouton est cliqué
def ouvre_fenetre_ajouter():
    fenetre_ajouter = tk.Toplevel()
    titre_fenetre_ajouter = tk.Label(fenetre_ajouter, text="Entrer les donnees")
    titre_fenetre_ajouter.pack()

    # Création des cinq zones de saisie
    label1 = tk.Label(fenetre_ajouter, text="Enter la référence du produit :")
    label1.pack()
    tk_reference = tk.Entry(fenetre_ajouter)
    tk_reference.pack()

    label2 = tk.Label(fenetre_ajouter, text="Enter le libelle du produit :")
    label2.pack()
    tk_libelle = tk.Entry(fenetre_ajouter)
    tk_libelle.pack()

    label3 = tk.Label(fenetre_ajouter, text="Enter la discription du produit :")
    label3.pack()
    tk_discription = tk.Entry(fenetre_ajouter)
    tk_discription.pack()

    label4 = tk.Label(fenetre_ajouter, text="Enter la quantité dans le stock du produit :")
    label4.pack()
    tk_quantite = tk.Entry(fenetre_ajouter)
    tk_quantite.pack()

    label5 = tk.Label(fenetre_ajouter, text="Enter le type du produit :")
    label5.pack()
    tk_type = tk.Entry(fenetre_ajouter)
    tk_type.pack()

    label6 = tk.Label(fenetre_ajouter, text="Enter le prix du produit :")
    label6.pack()
    tk_prix = tk.Entry(fenetre_ajouter)
    tk_prix.pack()





    def ajouter_produit():
        tk_produit={'reference':tk_reference.get(), 'libelle':tk_libelle.get(), 'description':tk_discription.get(), 'quantite':tk_quantite.get(), 'type':tk_type.get(), 'prix':tk_prix.get()}
        
        if tk_reference.get()=='' or tk_libelle.get()=='' :
            messagebox.showerror("Erreur", "Le champ de référence ou libelle est vide. Veuillez entrer des valeurs.")
            fenetre_ajouter.destroy()
            return



        for produit in tk_produits:
            if produit["reference"] == tk_reference.get():
                messagebox.showerror("Erreur", "Une référence similaire existe déjà. Veuillez entrer une autre référence.")
                fenetre_ajouter.destroy()
                return
        
        
        
        tk_produits.append(tk_produit)
        messagebox.showinfo("Ajout Réussi", "Le produit a été ajouté avec succès!")
        fenetre_ajouter.destroy()
    
    bouton_ajouter = tk.Button(fenetre_ajouter, text="Ajouter",command=ajouter_produit) 
    bouton_ajouter.pack()

    
def ouvre_list():
    fenetre_liste = tk.Toplevel()
    titre_fenetre_list = tk.Label(fenetre_liste, text="Affichage de la liste de produits")
    titre_fenetre_list.pack()


    tree = ttk.Treeview(fenetre_liste)
    tree["columns"] = ("reference", "libelle", "description", "quantite", "type", "prix")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("reference", anchor=tk.W, width=10)
    tree.column("libelle", anchor=tk.CENTER, width=50)
    tree.column("description", anchor=tk.CENTER, width=100)
    tree.column("quantite", anchor=tk.CENTER, width=10)
    tree.column("type", anchor=tk.CENTER, width=50)
    tree.column("prix", anchor=tk.CENTER, width=10)

    # En-têtes de colonne
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("reference", text="Reference", anchor=tk.W)
    tree.heading("libelle", text="Libelle", anchor=tk.CENTER)
    tree.heading("description", text="Description", anchor=tk.CENTER)
    tree.heading("quantite", text="Quantite", anchor=tk.CENTER)
    tree.heading("type", text="Type", anchor=tk.CENTER)
    tree.heading("prix", text="Prix", anchor=tk.CENTER)
    

# Ajout des produits dans le Treeview
    for i, produit in enumerate(tk_produits, start=1):
        tree.insert("", "end", text=str(i), values=(produit["reference"], produit["libelle"],produit["description"],produit["quantite"],produit["type"], produit["prix"]))

    
    # Affichage du Treeview
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def modi_pro():
    fenetre_modifier = tk.Toplevel()
    titre_fenetre_modifier = tk.Label(fenetre_modifier, text="Modifier un produit")
    titre_fenetre_modifier.pack()

    label = tk.Label(fenetre_modifier, text="Enter la référence du produit à modifier :")
    label.pack()
    tk_reference_mod = tk.Entry(fenetre_modifier)
    tk_reference_mod.pack()
    
    def verifier_ref():
      

        if tk_reference_mod.get()=='' :
            messagebox.showerror("Erreur", "Le champ de référence est vide. Veuillez entrer une valeur.")
            fenetre_modifier.destroy()
            return
        trv=False
        for produit in tk_produits:
            if produit["reference"] == tk_reference_mod.get():
                trv=True

                i=tk_produits.index(produit)
                messagebox.showinfo("Trouvé!","Entrer les nouvelles valeurs.")

                fenetre_mod = tk.Toplevel()
                titre_fenetre_mod = tk.Label(fenetre_mod, text="Entrer les nouvelles valeurs ")
                titre_fenetre_mod.pack()

                
                label1_3 = tk.Label(fenetre_mod, text="Enter la référence du produit :")
                label1_3.pack()
                tk_reference_3 = tk.Entry(fenetre_mod)
                tk_reference_3.insert(0,produit["reference"])
                tk_reference_3.pack()

                label2_3 = tk.Label(fenetre_mod, text="Enter le libelle du produit :")
                label2_3.pack()
                tk_libelle_3 = tk.Entry(fenetre_mod)
                tk_libelle_3.insert(0,produit["libelle"])
                tk_libelle_3.pack()

                label3_3 = tk.Label(fenetre_mod, text="Enter la discription du produit :")
                label3_3.pack()
                tk_discription_3 = tk.Entry(fenetre_mod)
                tk_discription_3.insert(0,produit["description"])
                tk_discription_3.pack()

                label4_3 = tk.Label(fenetre_mod, text="Enter la quantité en stock du produit :")
                label4_3.pack()
                tk_quantite_3 = tk.Entry(fenetre_mod)
                tk_quantite_3.insert(0,produit["quantite"])
                tk_quantite_3.pack()

                label5_3 = tk.Label(fenetre_mod, text="Enter le type du produit :")
                label5_3.pack()
                tk_type_3 = tk.Entry(fenetre_mod)
                tk_type_3.insert(0,produit["type"])
                tk_type_3.pack()

                label6_3 = tk.Label(fenetre_mod, text="Enter le prix du produit :")
                label6_3.pack()
                tk_prix_3 = tk.Entry(fenetre_mod)
                tk_prix_3.insert(0,produit["prix"])
                tk_prix_3.pack()   

                fenetre_modifier.destroy()


                def mod_ajt():
                    if tk_reference_3.get()==''  :
                        messagebox.showerror("Erreur", "Le champ de référence est vide. Veuillez entrer une valeur.")
                        return
                    
                    response = messagebox.askquestion("Question", "Confirmer la modification ?  ")
                    if response == "yes":

                        tk_produits[i]['reference']=tk_reference_3.get()
                        tk_produits[i]['libelle']=tk_libelle_3.get()
                        tk_produits[i]['description']=tk_discription_3.get()
                        tk_produits[i]['quantite']=tk_quantite_3.get()
                        tk_produits[i]['type']=tk_type_3.get()
                        tk_produits[i]['prix']=tk_prix_3.get()
                        messagebox.showinfo("Modifié", "Le produit est modifié.")
                        fenetre_mod.destroy()

                def sup_pro():
                    response = messagebox.askquestion("Question", f"confirmer la suppression de produit avec la reference {produit['reference']}, et le libelle {produit['libelle']} ?  ")
                    if response == "yes":
                        tk_produits.remove(produit)
                        messagebox.showinfo("Supprimé !",f"Le produit avec la reference : {tk_reference_3.get()} , est supprimé .")
                        fenetre_mod.destroy()

                bouton_ajt = tk.Button(fenetre_mod, text="Modifier",command=mod_ajt) 
                bouton_ajt.pack()

                bouton_sup = tk.Button(fenetre_mod, text="Supprimer",command=sup_pro) 
                bouton_sup.pack()
                
                break
        if not trv:
            messagebox.showwarning("Le produit n'est pas trouvé",f"Le produit avec la reference : {tk_reference_mod.get()} , n'est pas trouvée .")
            fenetre_modifier.destroy()


    bouton_suivant = tk.Button(fenetre_modifier, text="Chercher",command=verifier_ref) 
    bouton_suivant.pack()

def sauvegarde():

    response = messagebox.askquestion("Question", "Sauvegarder ?  ")
    if response == "yes":
        with open('file.json','w') as file:
                dump(tk_produits,file)
                print('--------------')
                print('Sauvegarder')
                print('--------------')
        
def sauvegarde_quitter():
    response = messagebox.askquestion("Question", "Sauvegarder et quitter ?  ")
    if response == "yes":
        sauvegarde()
        print("sauvegarder et quitter")
        fenetre_main.quit()

def quitter():
    response = messagebox.askquestion("Question", "Quitter sans sauvegarder ?  ")
    if response == "yes":
        print("quitter")
        fenetre_main.quit()


def enregistrer_sous():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        # Écrire le contenu JSON dans le fichier sélectionné
        with open(file_path, 'w') as f:
            dump(tk_produits, f)
        print("Fichier JSON enregistré avec succès.")
        messagebox.showinfo("Enregistré !","Fichier JSON enregistré avec succès.")

def ouvrir():
    global tk_produits

    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        # Lire le contenu JSON du fichier sélectionné
        with open(file_path, 'r') as f:
            tk_produits = load(f)
        file_label.config(text="Fichier ouvert : " + file_path)    
        print("Fichier JSON ouvert avec succès.")
        messagebox.showinfo("Ouvert !","Fichier JSON ouvert avec succès.")
        
def nouveau():
    global tk_produits
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        # Écrire le contenu JSON dans le fichier sélectionné
        with open(file_path, 'w') as f:
            dump([], f)
        with open(file_path, 'r') as f:
            tk_produits = load(f)
        file_label.config(text="Fichier ouvert : " + file_path)    
        print("Noveau fichier JSON 'vide' crée avec succès.")
        messagebox.showinfo("Noveau", "Noveau fichier JSON 'vide' crée avec succès.")


# def tri_prix():


# Création du bouton avec une action définie
bouton1 = tk.Button(fenetre_main, text="Ajouter un Produit", command=ouvre_fenetre_ajouter)
bouton1.pack()

bouton2 = tk.Button(fenetre_main, text="Afficher tous les produits", command=ouvre_list)
bouton2.pack()

bouton3 = tk.Button(fenetre_main, text="Chercher un produit pour modifier ou suprimer", command=modi_pro)
bouton3.pack()

# bouton7 = tk.Button(fenetre_main, text="Chercher un produit pour modifier ou suprimer", command=tri_prix)
# bouton7.pack()

# bouton8 = tk.Button(fenetre_main, text="Chercher un produit pour modifier ou suprimer", command=tri_qnt)
# bouton8.pack()

# bouton9 = tk.Button(fenetre_main, text="Chercher un produit pour modifier ou suprimer", command=tri_nom)
# bouton9.pack()

# bouton4 = tk.Button(fenetre_main, text="Sauvgader et rester", command=sauvegarde)
# bouton4.pack()

# bouton5 = tk.Button(fenetre_main, text="Sauvgader et quitter", command=sauvegarde_quitter)
# bouton5.pack()

# bouton6 = tk.Button(fenetre_main, text="Quitter sans sauvgarder", command=quitter)
# bouton6.pack()



# Créer la barre de menu
menubar = tk.Menu(fenetre_main)

# Ajouter des options à la barre de menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Nouveau fichier .JSON", command=nouveau)
file_menu.add_command(label="Ouvrir", command=ouvrir)
file_menu.add_command(label="Enregistrer sous", command=enregistrer_sous)
file_menu.add_command(label="Enregistrer", command=sauvegarde)
file_menu.add_separator()
file_menu.add_command(label="Enregistrer et Quitter", command=sauvegarde_quitter)
file_menu.add_command(label="Quitter", command=quitter)
menubar.add_cascade(label="Fichier", menu=file_menu)

# Afficher la barre de menu
fenetre_main.config(menu=menubar)









# Lancement de la boucle principale de Tkinter pour afficher la fenêtre
fenetre_main.mainloop()
