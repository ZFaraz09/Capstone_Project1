from .models import Festival, Category
from datetime import date

def festival_context(request):
    """Context processor to add active festival and categories to all templates"""
    active_festival = Festival.objects.filter(
        is_active=True,
        start_date__lte=date.today(),
        end_date__gte=date.today()
    ).first()
    
    categories = Category.objects.all()
    
    return {
        'active_festival': active_festival,
        'all_categories': categories,
    }
