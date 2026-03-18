from django.shortcuts import render, get_object_or_404
from sonapur.models import Agenda, Program, CoverPage, TeamMember, Talent, FooterSettings

def home(request):
    """
    Main landing page view.
    Fetches all data for the home page. The 'View More' logic 
    (3 for Programs, 6 for Team, 3 for Talents) is handled 
    via Django template tags and CSS/JS in home.html.
    """
    # 1. Fetch Agendas (Objectives)
    agendas = Agenda.objects.all()
    
    # 2. Fetch all Programs, ordered by newest date first
    # Template will display 3 initially, then 'View More'
    programs = Program.objects.all().order_by('-date')
    
    # 3. Fetch the most recent Cover Page image for the Hero background
    cover = CoverPage.objects.last()
    
    # 4. Fetch all Team Members
    # Template will display 6 initially, then 'View More'
    team_members = TeamMember.objects.all()
    
    # 5. Fetch all Talents, ordered by newest upload first
    # Template will display 3 initially, then 'View More'
    talents = Talent.objects.all().order_by('-created_at')

    # 6. Fetch Footer Settings (Contact, Socials, Map)
    footer = FooterSettings.objects.first()

    context = {
        'agendas': agendas,
        'programs': programs,
        'cover': cover,
        'team_members': team_members,
        'talents': talents,
        'footer': footer,
    }

    return render(request, 'sonapur/home.html', context)

def program_detail(request, pk):
    """
    Detailed view for a single program triggered from the Program section.
    """
    program = get_object_or_404(Program, pk=pk)
    
    # Fetch footer settings for the detail page
    footer = FooterSettings.objects.first()
    
    context = {
        'program': program,
        'footer': footer,
    }
    
    return render(request, 'sonapur/program_detail.html', context)