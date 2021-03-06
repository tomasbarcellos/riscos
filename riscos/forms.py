from . import models
from django import forms

class FormPlanejamento(forms.ModelForm):
    class Meta:
        model = models.Planejamento
        fields = ("nr_inicio", "nr_fim",)
        labels = {
            "nr_inicio": 'Ano inicial do Planejamento',
            "nr_fim": 'Ano final do Planejamento'
        }
        widgets = {
            'nr_inicio': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ano início"
                }),
            'nr_fim': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ano fim"
                }),
        }

class FormCadeia(forms.ModelForm):
    class Meta:
        model = models.Cadeia
        fields = ("id_planejamento", "ds_cadeia",)
        labels = {
            "id_planejamento": 'Planejamento Estratégico',
            "ds_cadeia": 'Nome da cadeia'
        }
        widgets = {
            "id_planejamento": forms.Select(
                attrs={
                    "class": "selectpicker form-control"
                }),
            'ds_cadeia': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome da Cadeia"
                })
        }

class FormMacroprocesso(forms.ModelForm):
    class Meta:
        model = models.Macroprocesso
        fields = ("id_cadeia", "ds_macroprocesso",)
        labels = {
            "id_cadeia": 'Nome da cadeia',
            "ds_macroprocesso": 'Nome do macroprocesso'
        }
        widgets = {
            'id_cadeia': forms.Select(attrs={"class": "selectpicker form-control"}),
            "ds_macroprocesso": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do macroprocesso"})
        }

class FormProcesso(forms.ModelForm):
    class Meta:
        model = models.Processo
        fields = ("ds_processo",)
        labels = {
            "ds_processo": 'Nome do processo'
        }
        widgets = {
            "ds_processo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do processo"})
        }

class FormAtividade(forms.ModelForm): 
    class Meta: 
        model = models.Atividade 
        fields = ("nr_atividade", "ds_atividade", "ds_responsavel",) 
        labels = {
            "nr_atividade": "Ordem da atividade no fluxo", 
            "ds_atividade": 'Nome da atividade', 
            "ds_responsavel": "Área responsável" 
        } 
        widgets = { 
            "nr_atividade": forms.NumberInput(attrs={
                "class": "form-control"}
            ), 
            "ds_atividade": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Atividade"
            }), 
            "ds_responsavel": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Área"
            }) 
        } 
 
class FormRisco(forms.ModelForm):
    def __init__(self, processo, *args,**kwargs):
        super(FormRisco, self).__init__(*args,**kwargs)
        self.fields['id_atividade'].queryset = models.Atividade.objects.filter(id_processo=processo)

    class Meta:
        model = models.Risco
        fields = ("id_atividade", "ds_risco", "id_tipo_risco", "id_impacto", "id_probabilidade",)
        labels = {
            "id_atividade": "Atividade",
            "ds_risco": "Descrição do risco",
            "id_tipo_risco": "Tipo do risco",
            "id_impacto": "Impacto",
            "id_probabilidade": "Probabilidade"
        }
        widgets = {
            "id_atividade": forms.Select(attrs={"class": "selectpicker form-control"}),
            "ds_risco": forms.TextInput(attrs={"class": "form-control", "placeholder": "Descrição do risco"}),
            "id_tipo_risco": forms.Select(attrs={"class": "selectpicker form-control"}),
            "id_impacto": forms.Select(attrs={"class": "form-control"}),
            "id_probabilidade": forms.Select(attrs={"class": "form-control"})
        }

class FormCausaConsequencia(forms.ModelForm):
    class Meta:
        model = models.CausaConsequencia
        fields = ("ds_causa_consequencia", "ds_tipo", )
        labels = {"ds_causa_consequencia": "", "ds_tipo": ""}
        widgets = {
            "ds_causa_consequencia": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Descrição"}
            ),
            "ds_tipo": forms.Select(attrs={"class": "selectpicker form-control", "style":"display:none"}),
        }

class FormTratamento(forms.ModelForm):
    def __init__(self, risco, *args,**kwargs):
        super(FormTratamento, self).__init__(*args,**kwargs)
        self.fields['id_causa_consequencia'].queryset = models.CausaConsequencia.objects.filter(id_risco=risco)

    class Meta:
        model = models.Tratamento
        fields = ("id_causa_consequencia", "ds_controle", "ds_status", "ds_quem", "ds_porque",
                  "dt_quando", "ds_como", "ds_quanto",)
        labels = {
            "id_causa_consequencia": "Tratamento sobre:",
            "ds_status": "Status do tratamento",
            "ds_controle": "Descrição do tratamento",
            "ds_quem": "Quem?",
            "ds_porque": "Por que?",
            "dt_quando": "Quando?",
            "ds_como": "Como?",
            "ds_quanto": "Quanto?",
        }   
        widgets = {
            "id_causa_consequencia": forms.Select(
                attrs={"class": "selectpicker form-control"},
            ),
            "ds_status": forms.Select(
                attrs={"class": "selectpicker form-control"}
            ),
            "ds_controle": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Descreva o que será realizado"}
            ),
            "ds_quem": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Quem será o responsável?"}
            ),
            "ds_porque": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Por que isso será feito?"}
            ),
            "dt_quando": forms.DateInput(
                attrs={"class": "form-control datepicker"}, format="%d/%m/%Y", 
            ),
            "ds_como": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Como isso ocorrerá?"}
            ),
            "ds_quanto": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Quanto isso custará (R$) ?"}
            )
        }

class FormMonitoramento(forms.ModelForm):
    class Meta:
        model = models.Monitoramento
        fields = ("ds_status", "ds_justificativa",)
        labels = {
            "ds_status": "Status do tratamento:",
            "ds_justificativa": "Justificativa:",
        }   
        widgets = {
            "ds_status": forms.Select(
                attrs={"class": "selectpicker form-control"}
            ),
            "ds_justificativa": forms.Textarea(
                attrs={"class": "form-control", "rows": "2"},
            ),
        }

class FormConsulta(forms.Form):
    tipo = forms.ChoiceField(
        choices=[("1", "Processo",), ("2", "Risco",)],
        required=True,
        widget=forms.RadioSelect()
    )
    plan = forms.ModelChoiceField(
        required=False,
        label="Planejamento Estratégico",
        queryset=models.Planejamento.objects.all(),
        widget=forms.Select(attrs={"class":"form-control form-control-sm"})
    )
    cad = forms.ModelChoiceField(
        required=False,
        label="Cadeia",
        queryset=models.Cadeia.objects.all(),
        widget=forms.Select(attrs={"class":"form-control form-control-sm"})
    )
    macro = forms.ModelChoiceField(
        required=False,
        label="Macroprocesso",
        queryset=models.Macroprocesso.objects.all(),
        widget=forms.Select(attrs={"class":"form-control form-control-sm"})
    )
    proc = forms.CharField(
        required=False,
        max_length=150,
        label="Processo",
        widget=forms.TextInput(attrs={"class":"form-control form-control-sm"})
    )
    ativ = forms.CharField(
        required=False,
        label="Atividade",
        max_length=150,
        widget=forms.TextInput(attrs={"class":"form-control form-control-sm"})
    )
    risc = forms.CharField(
        required=False,
        max_length=150,
        label="Risco",
        widget=forms.TextInput(attrs={"class":"form-control form-control-sm"})
    )

class FormImportacao(forms.Form):
    xls_file = forms.FileField(
        widget=forms.FileInput(
            attrs={"accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, application/vnd.ms-excel.sheet.macroEnabled.12"}
        ),
        label=""
    )

class FormConfirmacao(forms.Form):
    confirmacao = forms.BooleanField(label="")
