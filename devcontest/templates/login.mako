<%def name="login_box()">
    % if not request.environ.get('REMOTE_USER'):
		% if c.error:
			<span class="strong">${c.error}</span><br/>
		% endif
        ${h.form(h.url_for(controller="auth", action="signin"), method="post")}
        <label for="login">Login:</label>${h.text('login')}<br/>
        <label for="password">Heslo:</label>${h.password('password')}<br/>
        ${h.submit('submit', 'Přihlásit')}
        ${h.end_form()}

        <p><a href=${h.url_for(controller="registration", action="index")}>&rang; Registrace</a></p>
    % else:
        Jste přihlášen jako <strong>${request.environ.get('REMOTE_USER').fname} ${request.environ.get('REMOTE_USER').lname} </strong>.
    % endif
</%def>
