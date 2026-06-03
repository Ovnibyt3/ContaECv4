# Task: Create Notification Model and CRUD API Endpoints

## Summary

Created a complete general notification system for ContaEC, including SQLAlchemy model, Pydantic schemas, and FastAPI CRUD endpoints.

## Files Created

### 1. `/home/z/my-project/backend/app/models/notification.py`
- `NotificationType` enum: info, warning, error, success, system
- `NotificationCategory` enum: general, billing, accounting, hr, license, security, system
- `NotificationPriority` enum: low, normal, high, urgent
- `Notification` model with all required fields:
  - id (UUID PK with PG_UUID/sqlite variant pattern)
  - company_id (nullable FK to companies)
  - user_id (nullable FK to users)
  - type, category, title, message, is_read, action_url, action_label
  - priority, expires_at, is_active, created_at, updated_at
  - Relationships: company, user

### 2. `/home/z/my-project/backend/app/schemas/notification.py`
- `NotificationCreate`: title, message, type, category, priority, optional user_id/company_id/action_url/action_label/expires_at
- `NotificationUpdate`: optional is_read, is_active
- `NotificationResponse`: all fields with `model_config = {"from_attributes": True}`
- `NotificationListResponse`: notifications list + unread_count

### 3. `/home/z/my-project/backend/app/api/v1/endpoints/notifications.py`
7 endpoints:
- `GET /notifications` - List notifications for current user (with filters, unread_count, expired filtering)
- `GET /notifications/unread-count` - Just the count
- `POST /notifications` - Create (admin only)
- `PUT /notifications/mark-all-read` - Mark all as read
- `PUT /notifications/{id}/read` - Mark single as read
- `PUT /notifications/{id}` - Update notification
- `DELETE /notifications/{id}` - Soft delete (admin only)

## Files Modified

### 4. `/home/z/my-project/backend/app/models/__init__.py`
- Added import of Notification, NotificationType, NotificationCategory, NotificationPriority
- Added to __all__ list

### 5. `/home/z/my-project/backend/app/api/v1/router.py`
- Added `notifications` to imports
- Added `api_router.include_router(notifications.router)`

## Verification

- All imports verified successfully
- Database table `notifications` created with all indexes and foreign keys
- All 7 routes registered under `/api/v1/notifications`
- Follows existing codebase patterns (PG_UUID, mapped_column, from_attributes, etc.)
