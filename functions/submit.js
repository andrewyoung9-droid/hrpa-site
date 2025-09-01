export const onRequestPost = async (context) => {
  const { request, env } = context;

  // 1) Read form data
  const formData = await request.formData();
  const name = (formData.get("name") || "Anonymous").toString();
  const contact = (formData.get("contact") || "").toString();
  const county = (formData.get("county") || "").toString();
  const urgency = (formData.get("urgency") || "normal").toString();
  const topic = (formData.get("topic") || "Other").toString();
  const message = (formData.get("message") || "").toString();
  const turnstileToken = (formData.get("cf-turnstile-response") || "").toString();

  // 2) Verify Turnstile anti-bot
  const verifyRes = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    body: new URLSearchParams({
      secret: env.TURNSTILE_SECRET_KEY,
      response: turnstileToken,
      remoteip: request.headers.get("CF-Connecting-IP") || "",
    }),
    headers: { "content-type": "application/x-www-form-urlencoded" },
  });
  const verify = await verifyRes.json();
  if (!verify.success) {
    return new Response("Verification failed.", { status: 400 });
  }

  // 3) Build email via MailChannels (available on Cloudflare)
  const html = `
    <h2>HPRA Help Request</h2>
    <p><strong>Name/Alias:</strong> ${escapeHtml(name)}</p>
    <p><strong>Contact:</strong> ${escapeHtml(contact)}</p>
    <p><strong>County:</strong> ${escapeHtml(county)}</p>
    <p><strong>Urgency:</strong> ${escapeHtml(urgency)}</p>
    <p><strong>Topic:</strong> ${escapeHtml(topic)}</p>
    <p><strong>Message:</strong></p>
    <pre style="white-space:pre-wrap">${escapeHtml(message)}</pre>
  `;

  const mail = {
    personalizations: [{ to: [{ email: env.DEST_EMAIL }] }],
    from: { email: env.FROM_EMAIL, name: "HPRA Website" },
    subject: "New HPRA help request",
    content: [{ type: "text/html", value: html }],
  };

  const mailRes = await fetch("https://api.mailchannels.net/tx/v1/send", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(mail),
  });

  if (!mailRes.ok) {
    const err = await mailRes.text();
    return new Response("Email failed: " + err, { status: 500 });
  }

  // 4) Redirect back to a thank-you (you can create /thanks.html)
  return Response.redirect(new URL("/get-help.html?sent=1", request.url), 303);
};

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, (ch) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch])
  );
}
