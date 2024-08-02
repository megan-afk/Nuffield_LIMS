from django.shortcuts import render
from .models import Extraction, Sample
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Sample as SampleForm
from .forms import Extraction as ExtractionForm
import requests
import xml.etree.ElementTree as ET
# Create your views here.


def IndexView(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('LIMS:index')
        # extract form parameters and create sample object
        sample_name = request.POST.get('sample_name', '')
        taxon_id = request.POST.get('taxon_id', '')
        taxon_id = int(taxon_id or 0)
        scientific_name = request.POST.get('scientific_name', '')
        date_collected = request.POST.get('date_collected', '')
        if '' in (sample_name, taxon_id, scientific_name, date_collected):
            pass
        else:
            s = Sample(sample_name=sample_name, taxon_id=taxon_id, scientific_name=scientific_name,
                       date_collected=date_collected)
            s.save()

    else:
        form = SampleForm()

    samples = Sample.objects.all()
    context = {
        "samples": samples,
        'form': form,
    }
    return render(request, "LIMS/index.html", context)


def DetailView(request, sample_id):
    if request.method == 'GET':
        # getting all the objects of sample.
        samples = Sample.objects.all()

    s = Sample.objects.get(pk=sample_id)
    if request.method == 'POST':
        form = ExtractionForm(request.POST, request.FILES)
        # extract form parameters and create extraction object
        extraction_name = request.POST.get('extraction_name', '')
        extraction_method = request.POST.get('extraction_method', '')
        extraction_date = request.POST.get('extraction_date', '')

        if '' in (extraction_name, extraction_method, extraction_date):
            pass
        else:
            e = Extraction(extraction_name=extraction_name, extraction_method=extraction_method, extraction_date=extraction_date, sample=s)
            e.save()

    else:
        form = ExtractionForm()


    context = {
        "sample": s,
        "sample_id": sample_id,
        'form': form,
    }

    exts = s.extraction_set.all()
    context["extractions"] = exts

    return render(request, "LIMS/sample_detail.html", context)



def ExtractionView(request, extraction_id):
    e = Extraction.objects.get(pk=extraction_id)
    context = {"extraction": e}

    qcs = e.qc_set.all()
    context["qcs"] = qcs

    seq = e.sequencing_set.all()
    context["sequencing"] = seq
    return render(request, "LIMS/extraction_detail.html", context)


def auto_complete(request):
    t_id = request.GET.get('t_id', '')
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=" + t_id + "&retmode=xml"
    response = requests.get(url)
    if response.text:

        return HttpResponse(xml_parser(response.text))
    else:
        return HttpResponse("ERROR")


def xml_parser(xml):
    if xml == None:
        return False
    tree = ET.ElementTree(ET.fromstring(xml))
    root = tree.getroot()
    for child in root:
        if child.tag == "Taxon":
            ScientificName = child.find("ScientificName").text

            for subchild in child:
                if subchild.tag == "OtherNames":
                    GenbankCommonName = subchild.find("GenbankCommonName").text
                    return GenbankCommonName, ScientificName
