# Tom Boone Portfolio Backend

FastAPI backend for [tomboone.com](https://tomboone.com/) portfolio website.

## Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Environment setup:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Database setup:**
   ```bash
   alembic upgrade head
   ```

4. **Run development server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Authentication

This API uses **Microsoft Entra ID (Azure AD)** for authentication. Admin operations require proper Azure AD authentication with the `Admin` role or `admin` scope.

### Azure AD Setup

1. **Create App Registration** in Azure Portal:
   - Go to Azure Active Directory > App registrations > New registration
   - Set redirect URI for your frontend application
   - Note the Application (client) ID and Directory (tenant) ID

2. **Configure API Permissions**:
   - Add `User.Read` permission
   - Create custom scopes: `admin` and `read`

3. **Create App Roles**:
   - Add "Admin" role for administrative access
   - Assign users to the Admin role

4. **Configure Environment Variables**:
   
   **For Azure App Service:**
   ```bash
   AZURE_TENANT_ID=your-tenant-id
   AZURE_CLIENT_ID=your-client-id
   USE_MANAGED_IDENTITY=true
   ```
   
   **For Local Development or Non-Azure Hosting:**
   ```bash
   AZURE_TENANT_ID=your-tenant-id
   AZURE_CLIENT_ID=your-client-id
   USE_MANAGED_IDENTITY=false
   AZURE_CLIENT_SECRET=your-client-secret
   ```

### Authentication Flow

1. **Frontend authenticates** with Azure AD
2. **Receives access token** with appropriate scopes/roles
3. **Sends token** in Authorization header: `Bearer TOKEN`
4. **API validates token** against Azure AD and checks permissions

## API Endpoints

### Public (No Auth Required)
- `GET /api/v1/profile/` - Get first profile
- `GET /api/v1/profile/{id}` - Get specific profile

### Admin Only (Azure AD Required)
- `POST /api/v1/profile/` - Create profile
- `PUT /api/v1/profile/{id}` - Update profile
- `DELETE /api/v1/profile/{id}` - Delete profile
- `POST /api/v1/profile/full` - Create profile with relations
- `PUT /api/v1/profile/full/{id}` - Update profile with relations

### Authentication Endpoints
- `GET /auth/.well-known/openid-configuration` - Azure AD configuration
- `GET /auth/login` - Login redirect to Azure AD
- `GET /auth/logout` - Logout redirect

## Deployment

### Azure App Service

1. **Enable System-assigned Managed Identity**:
   - In Azure App Service > Identity > System assigned > Status: On
   - Note the Object (principal) ID

2. **Grant Azure AD permissions to Managed Identity**:
   - In your App Registration > API permissions
   - Add the managed identity as an authorized client

3. **Configure Environment Variables** in Azure App Service:
   ```bash
   AZURE_TENANT_ID=your-tenant-id
   AZURE_CLIENT_ID=your-client-id
   USE_MANAGED_IDENTITY=true
   DATABASE_URL=your-database-connection-string
   ```

4. **Configure CORS origins** for your frontend domain

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.