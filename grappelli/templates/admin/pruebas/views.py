def vote(request, presupuesto_id):
    p = get_object_or_404(Presupuesto, pk=presupuesto_id)
    try:
        selected_choice = p.detalle_set.get(pk=request.POST['detalle'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'presupuesto': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.total += selected_choice.precio
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
     #  return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

