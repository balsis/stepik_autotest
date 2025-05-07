from typing import Any, Dict, List

from pydantic import BaseModel


class Meta(BaseModel):
    page: int
    has_next: bool
    has_previous: bool


class Enrollment(BaseModel):
    id: int
    course: int


class ViewReports(BaseModel):
    enabled: bool
    needs_permission: str


class EditReports(BaseModel):
    enabled: bool
    needs_permission: str


class ViewGradeBookPage(BaseModel):
    enabled: bool
    needs_permission: str


class ViewGradeBook(BaseModel):
    enabled: bool
    needs_permission: str


class EditLti(BaseModel):
    enabled: bool
    needs_permission: str


class EditAdvancedSettings(BaseModel):
    enabled: bool
    needs_permission: str


class ManagePermissions(BaseModel):
    enabled: bool
    needs_permission: str


class ViewRevenue(BaseModel):
    enabled: bool


class CanBeBought(BaseModel):
    enabled: bool


class CanBePriceChanged(BaseModel):
    enabled: bool


class CanBeDeleted(BaseModel):
    enabled: bool


class EditTags(BaseModel):
    enabled: bool


class Actions(BaseModel):
    view_reports: ViewReports
    edit_reports: EditReports
    view_grade_book_page: ViewGradeBookPage
    view_grade_book: ViewGradeBook
    edit_lti: EditLti
    edit_advanced_settings: EditAdvancedSettings
    manage_permissions: ManagePermissions
    view_revenue: ViewRevenue
    can_be_bought: CanBeBought
    can_be_price_changed: CanBePriceChanged
    can_be_deleted: CanBeDeleted
    edit_tags: EditTags


class Course(BaseModel):
    id: int
    summary: str
    workload: str
    cover: str
    intro: str
    course_format: str
    target_audience: str
    certificate_footer: Any
    certificate_cover_org: str
    is_certificate_issued: bool
    is_certificate_auto_issued: bool
    certificate_regular_threshold: int
    certificate_distinction_threshold: int
    instructors: List[int]
    certificate: str
    requirements: str
    description: str
    sections: List[int]
    total_units: int
    enrollment: int
    is_favorite: bool
    actions: Actions
    progress: str
    first_lesson: int
    first_unit: int
    certificate_link: Any
    certificate_regular_link: Any
    certificate_distinction_link: Any
    user_certificate: Any
    referral_link: Any
    schedule_link: str
    schedule_long_link: str
    first_deadline: Any
    last_deadline: Any
    subscriptions: List[str]
    announcements: List[int]
    is_contest: bool
    is_self_paced: bool
    is_adaptive: bool
    is_idea_compatible: bool
    is_in_wishlist: bool
    last_step: str
    intro_video: Any
    social_providers: List
    authors: List[int]
    tags: List[int]
    has_tutors: bool
    is_enabled: bool
    is_proctored: bool
    proctor_url: Any
    review_summary: int
    schedule_type: str
    certificates_count: int
    learners_count: int
    lessons_count: int
    quizzes_count: int
    challenges_count: int
    peer_reviews_count: int
    instructor_reviews_count: int
    videos_duration: int
    time_to_complete: int
    is_popular: bool
    is_processed_with_paddle: bool
    is_unsuitable: bool
    is_paid: bool
    price: Any
    currency_code: Any
    display_price: str
    default_promo_code_name: Any
    default_promo_code_price: Any
    default_promo_code_discount: Any
    default_promo_code_is_percent_discount: Any
    default_promo_code_expire_date: Any
    continue_url: str
    readiness: float
    is_archived: bool
    options: Dict[str, Any]
    price_tier: Any
    position: int
    is_censored: bool
    difficulty: str
    acquired_skills: List[str]
    acquired_assets: List[str]
    learning_format: str
    content_details: List
    issue: Any
    course_type: str
    possible_type: Any
    is_certificate_with_score: bool
    preview_lesson: Any
    preview_unit: Any
    possible_currencies: List
    commission_basic: Any
    commission_promo: Any
    with_certificate: bool
    child_courses: List
    child_courses_count: int
    parent_courses: List
    became_published_at: str
    became_paid_at: Any
    title_en: str
    last_update_price_date: Any
    owner: int
    language: str
    is_featured: bool
    is_public: bool
    canonical_url: str
    title: str
    slug: str
    begin_date: Any
    end_date: Any
    soft_deadline: Any
    hard_deadline: Any
    grading_policy: str
    begin_date_source: Any
    end_date_source: Any
    soft_deadline_source: Any
    hard_deadline_source: Any
    grading_policy_source: str
    is_active: bool
    create_date: str
    update_date: str
    learners_group: Any
    testers_group: Any
    moderators_group: Any
    assistants_group: Any
    teachers_group: Any
    admins_group: Any
    discussions_count: int
    discussion_proxy: str
    discussion_threads: List[str]
    lti_consumer_key: str
    lti_secret_key: str
    lti_private_profile: bool


class Enrollments(BaseModel):
    meta: Meta
    enrollments: List[Enrollment]
    courses: List[Course]
