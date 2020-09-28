from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, request, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from Cadastro.forms import ATIForm, MercForm, AnexoForm
from Cadastro.management.commands.scrapy import Command
from Cadastro.models import ATI, CNT, Anexos


def index(request):
    return render(request, 'index.html', {})

def base(request):
    return render(request, 'anexoedit.html', {})


class ATIUpdate(UpdateView):
    model = ATI
    template_name = 'formsUpdate.html'
    form_class = ATIForm
    prefix = 'FormConhec'

    def get_context_data(self, **kwargs):
        context = super(ATIUpdate, self).get_context_data(**kwargs)
        Formset = modelformset_factory(CNT, form=MercForm, extra=0, min_num=1, max_num=20, can_delete=True)
        ati = (context['object'])
        try:
            instanceAnexoBL = Anexos.objects.filter(ATI_ANEXO=ati.pk, tipo='BL')
            instanceAnexoCE = Anexos.objects.filter(ATI_ANEXO=ati.pk, tipo='CE')
            instanceAnexoDT = Anexos.objects.filter(ATI_ANEXO=ati.pk, tipo='DT')
            instanceAnexoIV = Anexos.objects.filter(ATI_ANEXO=ati.pk, tipo='IV')
            instanceAnexoOT = Anexos.objects.filter(ATI_ANEXO=ati.pk, tipo='OT')
        except Anexos.DoesNotExist:
            instanceAnexoBL = None
            instanceAnexoCE = None
            instanceAnexoDT = None
            instanceAnexoIV = None
            instanceAnexoOT = None


        context['formMerc'] = Formset(queryset=CNT.objects.filter(ID_CNT_id=self.kwargs['pk']), prefix='FormMerc')
        context['formAnexo'] = instanceAnexoBL
        context['formAnexoMore'] = AnexoForm(prefix="c")
        context['formAnexoCE'] = instanceAnexoCE
        context['formAnexoCEMore'] = AnexoForm(prefix="b")
        context['formAnexoCEMore'] = AnexoForm(prefix="b")
        context['formAnexoCEMore'] = AnexoForm(prefix="b")
        return context

    def get_success_url(self):
        return reverse_lazy('update', kwargs={"pk": self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        anexo = self.request.FILES
        instanceATI = ATI.objects.get(pk=self.kwargs['pk'])
        Formset = modelformset_factory(CNT, form=MercForm, extra=1, min_num=1, max_num=20, can_delete=True)

        formCNT = Formset(request.POST, prefix='FormMerc')
        formCE = ATIForm(request.POST, prefix='FormConhec', instance=instanceATI)

        #FAZENDO UPDATE DA ATI
        if formCE.is_valid():
            idATI = formCE.save()

        if formCNT.is_valid():
            for formset in formCNT:
                ObjCNT = formset.save(commit=False)
                ObjCNT.ID_CNT = idATI
                ObjCNT.save()

        file_objs = anexo.getlist('arquivo')

        for file_obj in file_objs:
            anexo = Anexos.objects.create(arquivo=file_obj)
            anexoUp = Anexos.objects.get(pk=anexo.pk)
            anexoUp.ATI_ANEXO = idATI
            anexoUp.save()

        return HttpResponseRedirect(self.get_success_url())



def deleteAnexo(request, pk):

    if request.method == 'GET':
        previus = request.META.get('HTTP_REFERER')
        anexo = Anexos.objects.get(pk=pk or None)
        anexo.delete()

    return redirect(previus)


def delete_cnt_item(request):# meets the ajax request

    if len(request.POST) >= 0:
        cnt_id = int(request.POST['cnt'])
        CNT.objects.filter(id=cnt_id).delete()
        return HttpResponse()
    else:
        return HttpResponse()



class ListATI(ListView):

    model = ATI
    queryset = ATI.objects.all()
    template_name = 'teste.html'


def forms(request):

    if request.method == 'POST' and 'add_object2' in request.POST:
        objCE = request.POST.get('add_object2')

        if objCE != '':
            ce = request.POST['add_object2']
            scrapy = Command.handle(ce)
            ScrapyCapa = scrapy[0]
            ScrapyMerc = scrapy[1]

            form = ATIForm(prefix='FormConhec')
            form.fields["BL"].initial = ScrapyCapa['Número BL do Conhecimento de Embarque Original :']
            form.fields["CE"].initial = ce
            form.fields["REPCNPJ"].initial = ScrapyCapa['CNPJ :']
            form.fields["REPREZAO"].initial = ScrapyCapa['Razão Social :']

            #formStatus = StatusForm(prefix='StatusForm')
            form.fields["EMISSAO"].initial = ScrapyCapa['Data de Emissão do BL :']
            form.fields["SITUACAO"].initial = ScrapyCapa['Situação :']
            form.fields["MODALIDADE"].initial = ScrapyCapa['Modalidade de Frete :']
            form.fields["pORIGEM"].initial = ScrapyCapa['Porto de Origem :']
            form.fields["psPROCEDE"].initial = ScrapyCapa['País de Procedência :']
            form.fields["UFdestino"].initial = ScrapyCapa['UF de Destino Final :']


            Formset = modelformset_factory(CNT, form=MercForm)
            formMerc = Formset(queryset=CNT.objects.none(), initial=[
                {
                  'CNT': ScrapyMerc[0][index],
                  'cntISO': ScrapyMerc[1][index],
                  'cntTipo': ScrapyMerc[2][index],
                  'cntTara': ScrapyMerc[3][index],
                  'cntPB': ScrapyMerc[4][index],
                  'm3': ScrapyMerc[5][index],
                  'codIMO:': ScrapyMerc[6][index],
                  'clasIMO': ScrapyMerc[7][index]
                  } for index, i in enumerate(ScrapyMerc[0])
            ])
            formMerc.prefix='merda'
            a =len(ScrapyMerc[0])
            formMerc.extra = a

            formsetAnexo = modelformset_factory(Anexos, AnexoForm, extra=1)
            formAnexo = formsetAnexo(queryset=Anexos.objects.none(), prefix='form2')

            return render(request, 'forms.html', {'form': form, 'formMerc': formMerc, 'formAnexo': formAnexo})

    formsetPost = request.POST.get('merda-0-CNT')
    if formsetPost != '' and formsetPost != None:

        Formset = modelformset_factory(CNT, form=MercForm)
        formCNT = Formset(request.POST, prefix='merda')
        formCE = ATIForm(request.POST, prefix='FormConhec')

        formAnexos = request.FILES

        formAnexoBL = formAnexos.getlist('formAnexoBL-arquivo')
        formAnexoCE = formAnexos.getlist('formAnexoCE-arquivo')
        formAnexoDT = formAnexos.getlist('formAnexoDT-arquivo')
        formAnexoIV = formAnexos.getlist('formAnexoIV-arquivo')
        formAnexoOT = formAnexos.getlist('formAnexoOT-arquivo')

        if formCE.is_valid():
            idATI = formCE.save()

        if formCNT.is_valid():
            for formset in formCNT:
                ObjCNT = formset.save(commit=False)
                ObjCNT.ID_CNT = idATI
                ObjCNT.save()

        #file_objs = formAnexo.getlist('form2-0-arquivo')

        """for obj in file_objs:
            anexo = Anexos.objects.create(arquivo=obj)
            anexoUp = Anexos.objects.get(pk=anexo.pk)
            anexoUp.ATI_ANEXO = idATI
            anexoUp.save()"""

        for obj in formAnexoBL:
            anexo = Anexos.objects.create(arquivo=obj)
            anexoUp = Anexos.objects.get(pk=anexo.pk)
            anexoUp.ATI_ANEXO = idATI
            anexoUp.tipo = 'BL'
            anexoUp.save()

        for obj in formAnexoCE:
            anexo = Anexos.objects.create(arquivo=obj)
            anexoUp = Anexos.objects.get(pk=anexo.pk)
            anexoUp.ATI_ANEXO = idATI
            anexoUp.tipo = 'CE'
            anexoUp.save()

        return redirect('/update/' + str(idATI.pk))

    form = ATIForm(prefix='FormConhec')
    Formset = modelformset_factory(CNT, MercForm, extra=1)
    formMerc = Formset(queryset=CNT.objects.none(), prefix="merda")
    formsetAnexo = modelformset_factory(Anexos, AnexoForm, extra=1)
    #formAnexoBL = formsetAnexo(queryset=Anexos.objects.none(), prefix='form2')
    formAnexoBL = AnexoForm(prefix='formAnexoBL')
    formAnexoCE = AnexoForm(prefix='formAnexoCE')
    formAnexoDT = AnexoForm(prefix='formAnexoDT')
    formAnexoIV = AnexoForm(prefix='formAnexoIV')
    formAnexoOT = AnexoForm(prefix='formAnexoOT')

    return render(request, 'forms.html', {'form': form, 'formMerc': formMerc, 'formAnexoBL': formAnexoBL,
                                          'formAnexoCE': formAnexoCE, 'formAnexoDT': formAnexoDT,
                                          'formAnexoIV': formAnexoIV, 'formAnexoOT': formAnexoOT})






"""class ATIDetailView(DetailView):

    model = ATI
    template_name = 'forms.html'

    def get_context_data(self, **kwargs):
        Formset = modelformset_factory(CNT, form=MercForm, extra=0)
        form = ATIForm()

        context = super(ATIDetailView, self).get_context_data(**kwargs)
        context['form'] = form
        #context['formMerc'] = Formset
        ati = (context['object'])
        #cnts = CNT.objects.filter(ID_CNT_id__in=[ati.pk])
        context['formMerc'] = Formset(queryset=CNT.objects.filter(ID_CNT_id__in=[ati.pk]))


        form.fields["BL"].initial = ati.BL
        form.fields["CE"].initial = ati.CE
        form.fields["REPCNPJ"].initial = ati.REPCNPJ
        form.fields["REPREZAO"].initial = ati.REPREZAO
        form.fields["EMISSAO"].initial = ati.EMISSAO
        form.fields["SITUACAO"].initial = ati.SITUACAO
        form.fields["MODALIDADE"].initial = ati.MODALIDADE
        form.fields["pORIGEM"].initial = ati.pORIGEM
        form.fields["psPROCEDE"].initial = ati.psPROCEDE
        form.fields["UFdestino"].initial = ati.UFdestino
        return context"""

#O CODIGO ABAIXO FAZ O MESMO QUE A ATIUpate.view
"""def ATIUpdate(request, pk):
    instanceATI = ATI.objects.get(pk=pk)
    instanceMerc = CNT.objects.filter(ID_CNT__in=[pk])
    try:
        instanceAnexo = Anexos.objects.filter(ATI_ANEXO=pk)
    except Anexos.DoesNotExist:
        instanceAnexo = None

    if request.method == 'POST' and request.POST.get('formDelete') is not None:
        print()
    else:
        formATI = ATIForm(instance=instanceATI, prefix='formATI')
        Formset = modelformset_factory(CNT, form=MercForm)
        formMerc = Formset(queryset=instanceMerc, prefix='formMerc')
        formsetAnexo = modelformset_factory(Anexos, AnexoForm, extra=1)
        formAnexoNovo = formsetAnexo(queryset=Anexos.objects.none(), prefix='formAnexoN')
        formAnexo = instanceAnexo

        formsDict = {'formATI': formATI, 'formMerc': formMerc, 'formAnexoNovo': formAnexoNovo, 'formAnexo': formAnexo}
        return render(request, 'formsUpdate.html', formsDict)
"""

"""def form_valid(self, request):
    context = self.get_context_data()
    context['form2'] = self.request.FILES
    anexo = context['form2']
    #anexo = self.request.FILES
    file_objs = anexo.getlist('arquivo')

    for file_obj in file_objs:
        anexo = Anexos.objects.create(arquivo=file_obj)
        anexoUp = Anexos.objects.get(pk=anexo.pk)
        anexoUp.ATI_ANEXO = self.object
        anexoUp.save()

    #return HttpResponseRedirect(reverse('update', kwargs={"pk": self.object.pk}))
    #return super(ATIUpdate, self).form_valid(request)
    #return reverse_lazy('update', kwargs={"pk": self.object.pk})
    #return self.get_success_url()
    #return HttpResponseRedirect("")
    #return HttpResponseRedirect(self.get_success_url())
    previus = self.request.META.get('HTTP_REFERER')
    return redirect(previus)
    
    
    

    
def ATIUpdate(request, pk):
    instanceATI = ATI.objects.get(pk=pk)
    instanceMerc = CNT.objects.filter(ID_CNT__in=[pk])

    try:
        instanceAnexo = Anexos.objects.filter(ATI_ANEXO=pk)
    except Anexos.DoesNotExist:
        instanceAnexo = None

    if request.method == 'POST':
        form = ATIForm(request.POST, prefix='formATI')
        formMerc = MercForm(request.POST, prefix='formMerc')
        formAnexoNovo = request.FILES

        if form.is_valid():
            #idATI = ATI.objects.get(pk=pk)
            idATI = form
            idATI.save()

        if formMerc.is_valid():
            for formset in formMerc:
                ObjCNT = formset.save(commit=False)
                ObjCNT.ID_CNT = idATI
                ObjCNT.save()

        file_objs = formAnexoNovo.getlist('arquivo')
        for file_obj in file_objs:
            anexo = Anexos.objects.create(arquivo=file_obj)
            anexoUp = Anexos.objects.get(pk=anexo.pk)
            anexoUp.ATI_ANEXO = idATI
            anexoUp.save()

        formsDict = {'form': form, 'formMerc': formMerc, 'formAnexoNovo': formAnexoNovo}
        return render(request, 'formsUpdate.html', formsDict)

    else:
        form = ATIForm(instance=instanceATI, prefix='formATI')
        Formset = modelformset_factory(CNT, form=MercForm, extra=0)
        formMerc = Formset(queryset=instanceMerc, prefix='formMerc')
        formAnexo = instanceAnexo
        formAnexoNovo = AnexoForm(prefix='formAnexoN')

        formsDict = {'form': form, 'formMerc': formMerc, 'formAnexoNovo': formAnexoNovo, 'formAnexo': formAnexo}
        return render(request, 'formsUpdate.html', formsDict)"""

# form = self.form_class(initial=self.instanceATI, prefix='FormConhec')
# form = ATIForm(instance=instanceATI, prefix='FormConhec')
# formMerc = Formset(queryset=instanceMerc, prefix='FormMerc')
# formsetAnexo = modelformset_factory(Anexos, AnexoForm, extra=1)
# formAnexoNovo = formsetAnexo(queryset=Anexos.objects.none(), prefix='formAnexoN')
# formAnexo = instanceAnexo
# formsDict = {'form': form, 'formMerc': formMerc, 'formAnexoNovo': formAnexoNovo, 'formAnexo': formAnexo}
# return render(request, 'formsUpdate.html', formsDict)