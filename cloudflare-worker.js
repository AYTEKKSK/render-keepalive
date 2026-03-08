// Cloudflare Worker to route custom subdomains to Render services
// Deploy this at: https://dash.cloudflare.com/workers

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

// Mapping of subdomain -> Render service URL
const SUBDOMAIN_MAP = {
  'metal': 'https://metal-app-ocvv.onrender.com',
  'video': 'https://video-app-pqii.onrender.com',
  'doviz': 'https://doviz-app.onrender.com',
  'ceviri': 'https://ceviri-app.onrender.com',
  'haberler': 'https://haberler-app.onrender.com',
  'imsakiye': 'https://imsakiye-app.onrender.com',
  'namaz': 'https://namaz-app.onrender.com',
  'ocr': 'https://ocr-analiz-app.onrender.com',
  'yapay': 'https://yapay-zeka-app.onrender.com',
  'yemek': 'https://yemek-app.onrender.com',
  'gorsel': 'https://gorsel-app.onrender.com',
  'dosya': 'https://dosya-analizi-app.onrender.com',
  'donusturucu': 'https://donusturucu-app.onrender.com',
  'muzik': 'https://muzik-app-7q6u.onrender.com',
  'hava': 'https://hava-durumu-app-j89a.onrender.com'
}

async function handleRequest(request) {
  const url = new URL(request.url)
  const hostname = url.hostname
  
  // Extract subdomain (e.g., "metal" from "metal.articnc.online")
  const subdomain = hostname.split('.')[0]
  
  // Get target Render URL
  const targetUrl = SUBDOMAIN_MAP[subdomain]
  
  if (!targetUrl) {
    return new Response('Service not found', { status: 404 })
  }
  
  // Build new URL with same path and query string
  const targetFullUrl = targetUrl + url.pathname + url.search
  
  // Create new request with same method, headers, and body
  const modifiedRequest = new Request(targetFullUrl, {
    method: request.method,
    headers: request.headers,
    body: request.body,
    redirect: 'follow'
  })
  
  // Fetch from Render service
  try {
    const response = await fetch(modifiedRequest)
    
    // Create new response with CORS headers
    const modifiedResponse = new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers
    })
    
    // Add CORS headers
    modifiedResponse.headers.set('Access-Control-Allow-Origin', '*')
    modifiedResponse.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    modifiedResponse.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    
    return modifiedResponse
  } catch (error) {
    return new Response('Error fetching from origin: ' + error.message, { status: 502 })
  }
}
