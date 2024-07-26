<!-- IF USER DOES NOT HAVE CLIPCARD -->
% if current_user and not current_user.get('has_active_clipcard'):
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">KLIPPEKORT</p>
    <h2>Køb et klippekort</h2>
  </div>
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % for clipcard_key, clipcard_value in services_and_prices_content['clipcard_section']['clipcards']['clipcard_default'].items():
    <div>
      <div
        class="rounded-l-lg rounded-br-lg border-2 bg-unidYellow border-unidLightBlue flex flex-col"
      >
        <div class="flex flex-col lg:flex-row justify-between gap-6">
          <div class="text-unidPurple space-y-1 p-6">
            <p class="text-sm tracking-widest title-font font-medium">
              {{ clipcard_value["info"]["title"] }}
            </p>
            <h3>{{ clipcard_value["info"]["hours"] }}</h3>
          </div>
        </div>
        <div class="border-b border-unidLightBlue mx-6"></div>
        <div class="p-6 space-y-6">
          <div class="space-y-2">
            <!-- prettier-ignore -->
            % for point in clipcard_value['selling_points']:
            <div class="flex items-center gap-2 text-unidPurple">
              <div class="text-unidPurple w-5 h-5">
                % include(global_content['ui_icons']['checkmark'])
              </div>
              <p>{{ point["text"] }}</p>
            </div>
            % end
          </div>
          <div class="flex items-center justify-between gap-4">
            <p class="text-unidPurple text-base lg:text-lg">Pris</p>
            <div class="flex items-center gap-2">
              <p
                class="text-unidPurple text-right text-2xl xl:text-3xl font-saira font-bold"
              >
                {{ clipcard_value["info"]["price"] }}
              </p>
              <div class="flex flex-col text-xs text-unidPurple">
                <p>ekskl.</p>
                <p>moms</p>
              </div>
            </div>
          </div>
          <!-- Display button -->
          <button
            type="button"
            id="primary_button"
            class="buy-button"
            data-clipcard-type="{{ clipcard_value["info"]["title"] }}"
            data-clipcard-price="{{ clipcard_value["info"]["price"] }}"
          >
            {{ clipcard_value["button_text"] }}
          </button>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end
  </div>
</div>
% else:
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_clipcard"]["decorative_header_text"] }}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_clipcard"]["header_text"] }}
    </h2>
  </div>
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if tasks:
    % for task in tasks:
    <div id="content_box_styling">
      <div id="content_box_header_styling">
        <p id="content_box_header_text">{{ task["task_title"] }}</p>
      </div>
      <div class="flex flex-col gap-8 p-6 text-unidPurple">
        <!-- USER -->
        <div class="space-y-2 text-sm">
          <div class="space-y-1">
            <p id="form_label">Opgave oplysninger</p>
            <hr />
          </div>
          <div class="space-y-2">
            <div class="flex gap-2">
              <p class="font-semibold">Emne:</p>
              <p>{{ task["task_title"] }}</p>
            </div>
            <div class="space-y-2">
              <p class="font-semibold">Beskrivelse:</p>
              <p>{{ task["task_description"] }}</p>
            </div>
            <div class="flex gap-2">
              <p class="font-semibold">Tid brugt:</p>
              <p>{{ task["formatted_time_spent"] }}</p>
            </div>
            <div class="flex gap-2">
              <p class="font-semibold">Fuldført den:</p>
              <p>{{ task["formatted_created_at"] }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end
    % else:
    <div class="space-y-1">
      <p class="text-sm font-bold">
        Hov, du har ikke fået lavet noget endnu...
      </p>
      <p class="text-sm">
        Her vil du kunne få et overblik over hvilke opgaver, der er udført på
        dit klippekort.
      </p>
      <p class="text-sm">
        Klik på 'Beskeder' i menuen og skriv til os, hvad du vil have lavet!
      </p>
    </div>
    % end
  </div>
</div>
% end
