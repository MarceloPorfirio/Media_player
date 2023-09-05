import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

class Gradebook(ttk.Frame):
    def __init__(self,master_window):
        super().__init__(master_window,padding=(20, 10))# define o padding geral da tela 
        self.pack(fill=BOTH,expand=YES)

        self.name = ttk.StringVar(value="")
        self.student_id = ttk.StringVar(value="")
        self.course_name = ttk.StringVar(value="")
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors

        instruction_text = 'Entre com a informação de contato: '
        instruction = ttk.Label(self, text=instruction_text,width=50)
        instruction.pack(fill=X,pady=10) 

        # Chamar a função criada, passando os parametros necesários
        self.name_entry = self.create_form_entry("Nome: ",self.name,  r'^[a-zA-Z\s\']*$')
        self.create_form_entry("ID estudante: ",self.student_id,  r'^[0-9]*$')
        self.create_form_entry("Curso: ",self.course_name)

        # Foca o cursor na entrada de dados do nome
        self.name_entry.focus_set()
        
        #Aqui iremos atribuir a uma variavel, para poder manipular 
        self.final_score_input = self.create_form_entry("Pontuação Final: ",self.final_score)
        
        self.create_meter()
        self.create_buttonbox()
        self.table = self.create_table()

    # Crição de texto, numeral e inputs
    def create_form_entry(self,label,variable, regex=None):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X,expand=YES,pady=5)

        form_field_label = ttk.Label(master=form_field_container,text=label,width=15)
        form_field_label.pack(side=LEFT,padx=12)

        form_input = ttk.Entry(master=form_field_container,textvariable=variable)
        form_input.pack(side=LEFT,padx=5,fill=X,expand=YES)

        if regex:
            add_regex_validation(form_input, regex)

        return form_input
    
    # Criar o meter (giro_score)
    def create_meter(self):
        meter = ttk.Meter(
            master=self,
            metersize=150,
            padding=5,
            amounttotal=100,
            amountused=50,
            metertype="full",
            subtext="Pontuação Final",
            interactive=True,
        )
        meter.pack()
        # Usado para o input mudar os valores dentro do meter score
        
        self.final_score_input.configure(textvariable=meter.amountusedvar)
        self.final_score.set(meter.amountusedvar)
    
    # Criar os botões
    def create_buttonbox(self):
        button_container = ttk.Frame(self)
        button_container.pack(fill=X,expand=YES,pady=(15,10))

        cancel_btn = ttk.Button(
            master=button_container,
            text='Cancel',
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6
        )
        cancel_btn.pack(side=RIGHT,padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text='Submit',
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6 
        )
        submit_btn.pack(side=RIGHT,padx=5)
    
    # Cria a ação da função submit
    def on_submit(self):

        # pega o conteúdo dos campos de input
        nome = self.name.get()
        student = self.student_id.get()
        course = self.course_name.get()
        score = self.final_score_input.get()

        # mostra a mensagem de confirmação
        toast =ToastNotification(
            title='Cadastro feito com sucesso!',
            message='A pontuação foi adicionada com sucesso!',
            duration=3000,
        )
        toast.show_toast() # mostra a notificação

        #salva os dados na tabela

        self.data.append((nome,student,course,score))
        self.name.set("")  # Define o valor da StringVar como vazio
        self.student_id.set("")  # Define o valor da StringVar como vazio
        self.course_name.set("")  # Define o valor da StringVar como vazio
        self.final_score_input.delete(0, END)  # Limpa o valor atual do Entry
        self.final_score_input.insert(0, "50")  # Insere o valor anterior (50) no Entry
        

        self.table.destroy()
        self.table = self.create_table()

        # foca o cursor na entrada após o submit
        self.name_entry.focus_set()

        
        
        
    # Cria a ação da função cancelar
    def on_cancel(self):
        self.quit()

    def create_table(self):        

        # criação das colunas, stretch não deixa aumentar ou diminuir as colunas
        coldata = [
            {"text": "Nome"},
            {"text": "ID Estudante", "stretch": False},
            {"text": "Curso"},
            {"text": "Pontuação Final"}
        ]
        
        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data, # nosso data criado anteriormente
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            # stripecolor=(self.colors.light, None)
        )
        table.pack(fill=BOTH,expand=YES,padx=10,pady=10)

        return table

if __name__ == '__main__':
    app = ttk.Window('Gradebook','superhero',resizable=(False,False))
    Gradebook(app)
    app.mainloop()
