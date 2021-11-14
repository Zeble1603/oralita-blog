from django.utils.translation import gettext_lazy as _

class Locales:
    es= _("Español")
    fr= _("Francés")
    en= _("Inglés")
    ca= _("Catalán")
    it= _("Italiano")

class Global:
    site_name= _("Oralitá")
    name_label= _("nombre")
    phone_label= _("Teléfono")
    email_label= _("email")
    phone= _("937 978 493")
    email= _("info@oralita.com")
    address= _("Carrer de Vallirana, 28 08006 Barcelona")
    appointment= _("Pide tu cita")
    appointment_action= _("Pedir") 
    date= _("Fecha")
    hour= _("Hora")
    cancel= _("Anular")
    validate_captcha= _("Gracias por validar el captcha")
    footer=  _("""Copyright &copy; 2017 Oralitá | Made by <a href="http://www.david-courtey.com/" target="_blank">David Courtey</a>""")

class Default:
    title= _("Clínica Dental - Odontologia i Medicina Oral")
    og_title= _("Oralitá - Odontología y medicina oral italiana")
    og_description= _("Dr. Matteo Ricucci Odontólogo y responsable sanitario - Primera visita gratis")
    meta_description= _("Clínica Dental - Odontologia i Medicina Oral")
    meta_keywords= _("Clinica, Dental, Dentista, Barcelona, Odontologia, Oralitá, Medicina, Oral, Barcelona, Dr. Matteo Ricucci")

class Homepage:
    menu_page_name = _("Home")
    class slider_1:
        text=_("Clínica Dental - Oralitá")
        alt_img= _("photo clinica Dental Oralitá")
    class slider_2:
        text=_("Tu salud es nuestra misión, tu misión es sonreír")
        alt_img= _("nuestro dentista italiano Dr. Matteo Ricucci")
    class slider_3:
        text=_("")
        alt_img= _("photo clinica dental Oralitá")
    class slider_4:
        text=_("")
        alt_img= _("photo clinica dental Oralitá")
    class slider_5:
        text=_("")
        alt_img= _("photo clinica dental Oralitá")
    class services:
        class item_1:
            title = _("Primera visita")
            text = _("El diagnostico es el primer paso, el más importante. En Oralitá realizamos una primera visita completa, sin compromiso")
        class item_2:
            title = _("Radiologia digital")
            text = _("Para un correcto diagnostico, es imprescindible  una radiografía, por ello, ofrecemos a nuestros pacientes lo último en radiología digital, sin coste alguno.") 
        class item_3:
            title = _("Tratamientos pioneros")
            text = _(""" <ul style="text-align: left">
                            <li>Ortodoncia invisible</li>
                            <li>Prótesis sin metal</li>
                            <li>Blanqueamiento</li>
                        </ul>""") 
        class item_4:
            title = _("facilidades de pago")
            text = _("""<ul style="text-align: left">
                            <li>Pago por adelantado (10% descuento extra)</li>
                            <li>Financiación hasta 60 meses (12 meses sin intereses)</li>
                            <li>Pago fraccionado (según tratamiento realizado)</li>
                        </ul>""")     

        class about:
            title = _("PORQUE NOSOTROS:")
            sub_title = _("Damos la cara")
            text = _("Somos una clínica orientada a tratamientos  odontológicos integrales. Ofrecemos un amplio abanico de especialidades en medicina oral y un servicio personalizado  de confianza y  proximidad.")
            list = _("""<ul class="text-list" style="font-size: 18px;">
                            <li>Prevención</li>
                            <li>Equipo especializado</li>
                            <li>Calidad de materiales</li>
                            <li>Innovación</li>
                            <li>Proximidad</li>
                        </ul>""")

class Especialidades:
    menu_page_name = _("Especialidades")
    title = _("Nuestras especialidades")
    og_title = _("Oralitá - Nuestras especialidades")
    meta_description = _("Tu salud es nuestra misión, tu misión es sonreír")

class QuienesSomos:
    menu_page_name= _("Quienes somos")
    og_title= _("Oralitá - Quienes somos")
    og_description= _("Soy el Dr. Matteo Ricucci, dentista italiano licenciado en -Odontoiatria e protesi dentaria- por la universidad italiana de Pavia.")
    meta_description= _("Información sobre nuestro dentista Dr. Matteo Ricucci dentista italiano licenciado en -Odontoiatria e protesi dentaria- por la universidad italiana de Pavia.")
    meta_keywords= _("information, dentista, italiano, Odontoiatria, barcelona, odontólogo, doctor, Matteo Ricucci")
    title= _("Dr. Matteo Ricucci")
    sub_title= _("Odontólogo y responsable sanitario")
    alt_img_doctor= _("Matteo Ricucci Dentista Italiano")
    info= _("Colegiado COEC N°5657")
    text= _(""" <div class="doctor-text-quote">El éxito se consigue con trabajo, pasión, humildad y ante todo ética y respeto hacia las personas; es muy importante asesorar y entender cuales son las necesidades de cada uno para poder ofrecerle el tratamiento mas adecuado.
                    <div class="doctor-text-quote-quote"><img src="images/quote.png" alt="" /></div>
                </div>

                <p>Soy el Dr. Matteo Ricucci, dentista italiano licenciado en -Odontoiatria e protesi dentaria-  por la universidad italiana de Pavia. En 2008 decido mudarme a Barcelona y empezar mi carrera profesional; durante los últimos diez años he trabajado como especialista en prótesis y estética dental en diferentes clínicas de la ciudad y, gracias a los muchos tratamientos realizados, he podido perfeccionar mi técnica y crecer día tras día.</p>

                <p>La pasión por lo que hago y el perfeccionismo que me caracterizan han hecho primaria la necesidad de trabajar por cuenta propia; para conseguir resultados de calidad y con garantía de éxito es imperioso poder elegir material, instrumental clínico y metodología.</p>

                <p>De aquí se concretiza Oralitá, mi clínica dental, un proyecto hecho con todo el cariño y la ilusión de quien lo da todo para mejorar.</p>
            """)

class Donde:
    menu_page_name = _("Donde esta nuestra clinica dental")
    title= _("Donde esta nuestra clinica dental")
    og_title= _("Oralitá - Donde esta nuestra clinica dental")
    og_description= _("Información sobre cómo encontrarnos")
    meta_description= _("Información sobre cómo encontrarnos y hacer una cita con nuestro dentista")
    meta_keywords= _("information, cita, encontrarnos, dentista, barcelona, Gràcia, Lesseps")
    address= _("""<span>Carrer de Vallirana, 28 <br> 08006 Barcelona</span>""")
    how_to_come= _("Como llegar")
    class item_1 :
        title = _("Metro") 
        text = _("L3 Lesseps<br>L3 Fontana")
    class item_2 :
        title = _("FGC") 
        text = _("Sant Gervasi")
    class item_3 :
        title = _("Bus") 
        text = _("22, 24, 27, 32, V17, D40")   

class PrimeraVisita:
    menu_page_name=_("Primera visita")
    title=_("Primera visita")
    og_title=_("Oralitá - Primera visita gratis")
    og_description=_("""Oralitá il dentista italiano di Barcellona ti offre una prima visita gratuita con radiografía e sconti fino al 50% su molte prestazioni.""")
    sub_title=_("Ven a conocernos sin compromiso")
    meta_description=_("Ven a conocernos sin compromiso")
    meta_keywords=_("pedir, visita, sin compromiso")
    text=_("""El enfoque de una primera visita es valorar la salud bucodental del paciente bajo diferentes puntos de vista. Nuestra metodología consta en:
                <ul>
                    <li>Examinar  el estado de dientes y encías. Es necesario que tanto las caries como eventuales patologías gingivales sean tratadas para prevenir problemas mayores.</li>
                    <li>Comprobar la función masticatoria. Los dientes sirven para triturar , la ausencia de uno o mas de ellos y una mala oclusión, pueden alterar el proceso digestivo, generado diferentes patologías.</li>
                    <li>Estética. Si el paciente quiere mejorar la armonía de su sonrisa, disponemos de una serie de tratamientos que nos garantizan resultados excelentes sin comprometer la salud buco-dental.</li>
                </ul>""")

class Contact:
    menu_page_name=_("Contacto")
    title=_("Contacto y hacer una cita con nuestro dentista")
    og_title=_("Oralitá - Contacto y hacer una primera visita gratis")
    og_description=_("Oralitá il dentista italiano di Barcellona ti offre una prima visita gratuita con radiografía e sconti fino al 50% su molte prestazioni.")
    meta_description=_("Formulare de contacto en italiano o español")
    meta_keywords=_("contacto, formulare, cita, dentista, barcelona, dentista italiano, Gràcia, Lesseps")

class Thanks:
    title=_("Gracias de su solicitud")
    message=_("Su solicitud de cita ha sido enviada. Nos pondremos en contacto con usted lo antes posible")

class Form:
    title=_("Primera visita sin compromiso")
    error=_("Parece que te estás perdiendo alguna información. Inténtalo de nuevo.")
    success=_("Su solicitud de cita ha sido enviada. Nos pondremos en contacto con usted lo antes posible")
    message=_("Motivo de la visita...")

class Horario:
    title=_("HORARIO DE ATENCIÓN")
    extra=_("OTROS HORARIOS CON CITA PREVIA")
    class monday:
        name=_("Lunes")
        open=_("15h a 19h")
    class tuesday:
        name=_("Martes")
        open=_("10h a 19h")
    class wednesday:
        name=_("Miércoles")
        open=_("10h a 19h")
    class thursday:
        name=_("Jueves")
        open=_("10h a 19h")
    class friday:
        name=_("Viernes")
        open=_("10h a 14h")
    class saturday:
        name=_("Sábado")
        open=_("Cerrado")                    
    class sunday:
        name=_("Domingo")
        open=_("Cerrado")    