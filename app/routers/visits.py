from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_business
from app.models.business import Business
from app.schemas.visit import VisitCreate, VisitResponse
from app.services.visit_service import create_visit

router = APIRouter(prefix="/visits", tags=["Visits"])


@router.post("", response_model=VisitResponse)
def log_visit(
    visit_data: VisitCreate,
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """Log a completed visit. Updates customer stats automatically."""
    return create_visit(db, visit_data, business)
