// Simple email protection
function showContact() {
  var email = 'jobs.george' + String.fromCharCode(64) + 'protonmail.com';
  document.write('<a href="mailto:' + email + '">Contact</a>');
}
