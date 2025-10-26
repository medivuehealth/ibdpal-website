# Clean URL Setup Guide for IBDPal Website

## 🎯 **Objective**
Set up clean URLs like `ibdpal.org/support` and `ibdpal.org/privacy` instead of `support.html` and `privacy.html`.

## 📁 **Files Created/Modified**

### **1. Server Configuration Files**
- **`.htaccess`** - For Apache servers
- **`_redirects`** - For Netlify hosting
- **`vercel.json`** - For Vercel hosting

### **2. Updated HTML Files**
- **`index.html`** - Updated navigation links
- **`support.html`** - Updated navigation links  
- **`privacy.html`** - Updated navigation links
- **`terms.html`** - Updated navigation links

### **3. JavaScript Fallback**
- **`url-routing.js`** - Client-side routing fallback

## 🚀 **Deployment Options**

### **Option 1: Apache Server (.htaccess)**
If you're using Apache hosting, the `.htaccess` file will handle URL rewriting automatically.

### **Option 2: Netlify (_redirects)**
If deploying to Netlify, the `_redirects` file will handle the routing.

### **Option 3: Vercel (vercel.json)**
If deploying to Vercel, the `vercel.json` file will handle the routing.

### **Option 4: GitHub Pages**
For GitHub Pages, you'll need to use the JavaScript fallback by adding this to your HTML files:
```html
<script src="url-routing.js"></script>
```

## 🔧 **URL Mappings**

| Clean URL | HTML File | Description |
|-----------|-----------|-------------|
| `/` | `index.html` | Home page |
| `/support` | `support.html` | Support page |
| `/privacy` | `privacy.html` | Privacy policy |
| `/terms` | `terms.html` | Terms of service |
| `/about` | `executive-summary.html` | About/Executive summary |

## ✅ **What's Been Updated**

### **Navigation Links**
All navigation links now use clean URLs:
- Header navigation: `/privacy`, `/support`
- Footer links: `/privacy`, `/support`, `/terms`
- Logo links: `/` (home)

### **Cross-References**
All internal links have been updated to use clean URLs instead of `.html` files.

## 🧪 **Testing**

### **Local Testing**
1. Open `index.html` in a browser
2. Click on Privacy/Support links
3. Verify they work with clean URLs

### **Server Testing**
1. Deploy to your hosting platform
2. Test URLs: `yoursite.com/support`, `yoursite.com/privacy`
3. Verify they redirect to the correct HTML files

## 🛠️ **Troubleshooting**

### **If Clean URLs Don't Work:**
1. **Check server configuration** - Ensure your hosting platform supports URL rewriting
2. **Use JavaScript fallback** - Add `url-routing.js` to your HTML files
3. **Check file permissions** - Ensure `.htaccess` files are readable

### **For Static Hosting:**
If your hosting doesn't support server-side rewriting, the JavaScript fallback will handle the routing automatically.

## 📝 **Notes**

- **SEO Friendly**: Clean URLs are better for SEO
- **User Friendly**: Easier to remember and share
- **Professional**: Looks more professional than `.html` extensions
- **Consistent**: All internal links now use the same URL format

## 🎉 **Result**

Your website will now have clean, professional URLs:
- ✅ `ibdpal.org/support` (instead of `support.html`)
- ✅ `ibdpal.org/privacy` (instead of `privacy.html`)
- ✅ `ibdpal.org/terms` (instead of `terms.html`)
- ✅ `ibdpal.org/about` (instead of `executive-summary.html`)

All navigation and links have been updated to use these clean URLs!

