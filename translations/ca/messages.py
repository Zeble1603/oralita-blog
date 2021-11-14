from django.utils.translation import gettext_lazy as _

class LocalesCat:
    es= _("Castellà")
    fr= _("Francès")
    en= _("Anglès")
    ca= _("Català")
    it= _("Italià")

class GlobalCat:
    site_name= _("Oralitá")
    name_label= _("nom")
    phone_label= _("Telèfon")
    email_label= _("email")
    phone= _("937 978 493")
    email= _("info@oralita.com")
    address= _("Carrer de Vallirana, 28 08006 Barcelona")
    appointment= _("Demana la teva cita")
    appointment_action= _("Demana") 
    date= _("Data")
    hour= _("Hora")
    cancel= _("Anul·lar")
    validate_captcha= _("Gràcies per validar el captcha")
    footer=  _("""Copyright &copy; 2017 Oralitá | Made by <a href="http://www.david-courtey.com/" target="_blank">David Courtey</a>""")

class DefaultCat:
    title= _("Clínica Dental - Odontologia i Medicina Oral")
    og_title= _("Oralitá - Odontologia i medicina oral italiana")
    og_description= _("Dr. Matteo Ricucci odontòleg i responsable sanitari - Primera visita gratuïta")
    meta_description= _("Clínica Dental - Odontologia i Medicina Oral")
    meta_keywords= _("Clinica, Dental, Dentista, Barcelona, Odontologia, Oralitá, Medicina, Oral, Barcelona, Dr. Matteo Ricucci")

class HomepageCat:
    menu_page_name = _("Home")
    class slider_1:
        text=_("Clínica Dental - Oralitá")
        alt_img= _("photo clínica Dental Oralitá")
    class slider_2:
        text=_("Clínica Dental - Oralitá")
        alt_img= _("photo clínica Dental Oralitá")
    class slider_3:
        text=_("")
        alt_img= _("photo clínica dental Oralitá")
    class slider_4:
        text=_("")
        alt_img= _("photo clínica dental Oralitá")
    class slider_5:
        text=_("")
        alt_img= _("photo clínica dental Oralitá")
    class services:
        class item_1:
            title = _("Primera visita")
            text = _("El diagnòstic és el primer pas, el més important. En Oralitá realitzem una primera visita completa, sense compromís")
        class item_2:
            title = _("Radiologia digital")
            text = _("Per a un correcte diagnòstic, és imprescindible una radiografia, per això, oferim als nostres pacients l'últim en radiologia digital, sense cap cost.") 
        class item_3:
            title = _("Tractaments pioners")
            text = _(""" <ul style="text-align: left">
                            <li>Ortodòncia invisible </li>
                            <li>Pròtesis sense metall </li>
                            <li>Blanquejament</li>
                        </ul>""") 
        class item_4:
            title = _("facilitats de pagament")
            text = _("""<ul style="text-align: left">
                            <li>Pagament per avançat (10% descompte extra) </li>
                            <li>Finançament fins a 60 mesos (12 mesos sense interessos)</li>
                            <li>Pagament fraccionat (segons tractament realitzat) </li>
                        </ul>""")     

        class about:
            title = _("PERQUÈ NOSALTRES:")
            sub_title = _("Donem la cara")
            text = _("Som una clínica orientada a tractaments odontològics integrals. Oferim un ampli ventall d'especialitats en medicina oral i un servei personalitzat de confiança i proximitat.")
            list = _("""<ul class="text-list" style="font-size: 18px;">
                            <li>Prevenció</li>
                            <li>Equip especialitzat </li>
                            <li>Qualitat de materials </li>
                            <li>Innovació</li>
                            <li>Proximitat</li>
                        </ul>""")

class EspecialidadesCat:
    menu_page_name = _("Especialitats")
    title = _("Les nostres especialitats")
    og_title = _("Oralitá - Les nostres especialitats")
    meta_description = _("La teva salut és la nostra missió, la teva missió és somriure")

class QuienesSomosCat:
    menu_page_name= _("Qui som")
    og_title= _("Oralitá - Qui som")
    og_description= _("Sóc el Dr. Matteo Ricucci, dentista italià llicenciat en -Odontologìa i Pròtesi dental- per la universitat italiana de Pavia.")
    meta_description= _("Informació sobre el nostre dentista Dr. Matteo Ricucci dentista italià llicenciat en -Odontologìa i Pròtesi denta- per la universitat italiana de Pavia.")
    meta_keywords= _("informació, dentista, italià, odontologia, barcelona, odontòleg, metge, Matteo Ricucci")
    title= _("Dr. Matteo Ricucci")
    sub_title= _("Odontòleg i responsable sanitari")
    alt_img_doctor= _("Matteo Ricucci Dentista Italià")
    info= _("Colegiado COEC N°5657")
    text= _(""" <div class="doctor-text-quote">L'èxit s'aconsegueix amb treball, passió, humilitat i sobretot ètica i respecte cap a les persones; és molt important assessorar i entendre quines són les necessitats de cada un per poder oferir-li el tractament més adequat.
                    <div class="doctor-text-quote-quote"><img src="images/quote.png" alt="" /></div>
                </div>

                <p>Sóc el Dr. Matteo Ricucci, dentista italià llicenciat en -Odontologìa i Pròtesi dental- per la universitat italiana de Pavia. El 2008 decideixo mudar-me a Barcelona i començar la meva carrera professional; durant els últims deu anys he treballat com a especialista en pròtesis i estètica dental en diferents clíniques de la ciutat i, gràcies als molts tractaments realitzats, he pogut perfeccionar la meva tècnica i créixer dia rere dia. </p>

                <p>La passió pel que faig i el perfeccionisme que em caracteritzen han fet primària la necessitat de treballar per compte propi; per aconseguir resultats de qualitat i amb garantia d'èxit és imperiós poder triar material, instrumental clínic i metodologia. </p>

                <p>D'aquí es concreta Oralitá, la meva clínica dental, un projecte fet amb tot l'afecte i la il·lusió de qui ho dóna tot per millorar. </p>
            """)

class DondeCat:
    menu_page_name = _("On és la nostra clínica dental")
    title= _("On és la nostra clínica dental")
    og_title= _("Oralitá - On és la nostra clínica dental")
    og_description= _("Informació sobre com trobar-nos")
    meta_description= _("Informació sobre com trobar-nos i fer una cita amb el nostre dentista")
    meta_keywords= _("informació, cita, trobar-nos, dentista, barcelona, Gràcia, Lesseps")
    address= _("""<span>Carrer de Vallirana, 28 <br> 08006 Barcelona</span> """)
    how_to_come= _("Com arribar")
    class item_1 :
        title = _("Metro") 
        text = _("L3 Lesseps<br>L3 Fontana")
    class item_2 :
        title = _("FGC") 
        text = _("Sant Gervasi")
    class item_3 :
        title = _("Bus") 
        text = _("22, 24, 27, 32, V17, D40")   

class PrimeraVisitaCat:
    menu_page_name=_("Primera visita")
    title=_("Primera visita")
    og_title=_("Oralitá - Primera visita gratuïta")
    og_description=_("""Oralitá il dentista italiano di Barcellona ti offre una prima visita gratuita con radiografía e sconti fino al 50% su molte prestazioni.""")
    sub_title=_("Vine a conèixer-nos sense compromís")
    meta_description=_("Vine a conèixer-nos sense compromís")
    meta_keywords=_("demanar, visita, sense compromís")
    text=_("""L'enfocament d'una primera visita és valorar la salut bucodental del pacient sota diferents punts de vista. La nostra metodologia consta en:
            <ul>
                <li>Examinar l'estat de dents i genives. Cal que tant les càries com eventuals patologies gingivals siguin tractades per prevenir problemes majors.</li>
        

                <li>Comprovar la funció masticatòria. Les dents serveixen per triturar, l'absència d'un o més d'ells i una mala oclusió, poden alterar el procés digestiu, generat diferents patologies.</li> 
                <li>Estètica. Si el pacient vol millorar l'harmonia del seu somriure, disposem d'una sèrie de tractaments que ens garanteixen resultats excel·lents sense comprometre la salut bucodental.</li>
            </ul>""")

class ContactCat:
    menu_page_name=_("Contacte")
    title=_("Contacte i fer una cita amb el nostre dentista")
    og_title=_("Oralitá - Contacte i fer una primera visita gratuïta")
    og_description=_("Oralitá il dentista italiano di Barcellona ti offre una prima visita gratuita con radiografía e sconti fino al 50% su molte prestazioni.")
    meta_description=_("formula de contacte en italià o espanyol")
    meta_keywords=_("contacte, formula, cita, dentista, barcelona, dentista italià, Gràcia, Lesseps")

class ThanksCat:
    title=_("Gràcies de la seva sol·licitud")
    message=_("La seva sol.licitud de cita ha estat enviada. Ens posarem en contacte amb vostè el més aviat possible")

class FormCat:
    title=_("Primera visita sense compromís")
    error=_("Sembla que t'estàs perdent alguna informació. Intenta-ho de nou.")
    success=_("La seva sol.licitud de cita ha estat enviada. Ens posarem en contacte amb vostè el més aviat possible")
    message=_("Motiu de la visita ...")

class HorarioCat:
    title=_("HORARI D'ATENCIÓ")
    extra=_("ALTRES HORARIS AMB CITA PRÈVIA")
    class monday:
        name=_("Dilluns")
        open=_("15h a 19h")
    class tuesday:
        name=_("Dimarts")
        open=_("10h a 19h")
    class wednesday:
        name=_("Dimecres")
        open=_("10h a 19h")
    class thursday:
        name=_("Dijous")
        open=_("10h a 19h")
    class friday:
        name=_("Divendres")
        open=_("10h a 14h")
    class saturday:
        name=_("Dissabte")
        open=_("Tancat")                    
    class sunday:
        name=_("Diumenge")
        open=_("Tancat")     

            





