	{% comment %}
	<h2>For</h2>
		<p>
		{% for c in courses %}
			{{ c }} <br/>
		{% empty %}
			Нету курсов
		{% endfor%}		
		</p>

		<p>
		{% for i in instructors %}
			{% if forloop.first %}
				First
			{% elif forloop.last %}
				Last
			{% else %}
				{{ forloop.counter0 }} 
			{% endif %}

			{% cycle "+" "-" %}

			: {{ i }} <br/>
		{% endfor%}		
		</p>


		<p>
		<h2>Preprepre</h2>


		{{ var1|upper }} <br/> 
		{{ var2|lower }} <br/> 
		{% firstof asd instructors %}<br/> 
		{{ instructors|default:"nothing"|title }}<br/> 
		{{ template }}<br/>
		{{ var3 }} --- {{ var3|first }} --- {{ var3|last }} --- {{ var3|length }} --- {{ var3|slice:"1"}} --- {{ var3|slice:"1:"}} --- {{ var3.0}} --- {{ var3|length_is:"4" }} --- {{ var3|length_is:"2" }}<br/> 
		{{ var4 }} --- {{ var4.some_str }} --- {{ var4.some_str.0 }}
		
		</p>

		<p>
		{% filter title %}
		{# comment!!! #}

		{% comment %}
		tra-la-la
		{% endcomment %}

		{{ instructors.1.email }}
		sdf sdf sdffff. Some text. safas.  fDFGd.
		{% endfilter %}
		</p>

	{% endcomment %}